/**
 * @author Zhaonian Zou <znzou@hit.edu.cn>,
 * School of Computer Science and Technology,
 * Harbin Institute of Technology, China
 */

#include "executor.h"

#include <exceptions/buffer_exceeded_exception.h>
#include <cmath>
#include <ctime>
#include <functional>
#include <iostream>
#include <string>
#include <utility>

#include "file_iterator.h"
#include "page_iterator.h"
#include "storage.h"

using namespace std;

namespace badgerdb {

void TableScanner::print() const {
  badgerdb::File file = badgerdb::File::open(tableFile.filename());
  for (badgerdb::FileIterator iter = file.begin(); iter != file.end(); ++iter) {
    badgerdb::Page page = *iter;
    badgerdb::Page* buffered_page;
    bufMgr->readPage(&file, page.page_number(), buffered_page);

    for (badgerdb::PageIterator page_iter = buffered_page->begin();
         page_iter != buffered_page->end(); ++page_iter) {
      string key = *page_iter;
      string print_key = "(";
      int current_index = 0;
      for (int i = 0; i < tableSchema.getAttrCount(); ++i) {
        switch (tableSchema.getAttrType(i)) {
          case INT: {
            int true_value = 0;
            for (int j = 0; j < 4; ++j) {
              if (std::string(key, current_index + j, 1)[0] == '\0') {
                continue;  // \0 is actually representing 0
              }
              true_value +=
                  (std::string(key, current_index + j, 1))[0] * pow(128, 3 - j);
            }
            print_key += to_string(true_value);
            current_index += 4;
            break;
          }
          case CHAR: {
            int max_len = tableSchema.getAttrMaxSize(i);
            print_key += std::string(key, current_index, max_len);
            current_index += max_len;
            current_index +=
                (4 - (max_len % 4)) % 4;  // align to the multiple of 4
            break;
          }
          case VARCHAR: {
            int actual_len = key[current_index];
            current_index++;
            print_key += std::string(key, current_index, actual_len);
            current_index += actual_len;
            current_index +=
                (4 - ((actual_len + 1) % 4)) % 4;  // align to the multiple of 4
            break;
          }
        }
        print_key += ",";
      }
      print_key[print_key.size() - 1] = ')';  // change the last ',' to ')'
      cout << print_key << endl;
    }
    bufMgr->unPinPage(&file, page.page_number(), false);
  }
  bufMgr->flushFile(&file);
}

JoinOperator::JoinOperator(File& leftTableFile,
                           File& rightTableFile,
                           const TableSchema& leftTableSchema,
                           const TableSchema& rightTableSchema,
                           const Catalog* catalog,
                           BufMgr* bufMgr)
    : leftTableFile(leftTableFile),
      rightTableFile(rightTableFile),
      leftTableSchema(leftTableSchema),
      rightTableSchema(rightTableSchema),
      resultTableSchema(
          createResultTableSchema(leftTableSchema, rightTableSchema)),
      catalog(catalog),
      bufMgr(bufMgr),
      isComplete(false) {
  // nothing
}

TableSchema JoinOperator::createResultTableSchema(
    const TableSchema& leftTableSchema,
    const TableSchema& rightTableSchema) {
  vector<Attribute> attrs;

  // first add all the left table attrs to the result table
  for (int k = 0; k < leftTableSchema.getAttrCount(); ++k) {
    Attribute new_attr = Attribute(
        leftTableSchema.getAttrName(k), leftTableSchema.getAttrType(k),
        leftTableSchema.getAttrMaxSize(k), leftTableSchema.isAttrNotNull(k),
        leftTableSchema.isAttrUnique(k));
    attrs.push_back(new_attr);
  }

  // test every right table attrs, if it doesn't have the same attr(name and
  // type) in the left table, then add it to the result table
  for (int i = 0; i < rightTableSchema.getAttrCount(); ++i) {
    bool has_same = false;
    for (int j = 0; j < leftTableSchema.getAttrCount(); ++j) {
      if ((leftTableSchema.getAttrType(j) == rightTableSchema.getAttrType(i)) &&
          (leftTableSchema.getAttrName(j) == rightTableSchema.getAttrName(i))) {
        has_same = true;
      }
    }
    if (!has_same) {
      Attribute new_attr = Attribute(
          rightTableSchema.getAttrName(i), rightTableSchema.getAttrType(i),
          rightTableSchema.getAttrMaxSize(i), rightTableSchema.isAttrNotNull(i),
          rightTableSchema.isAttrUnique(i));
      attrs.push_back(new_attr);
    }
  }
  return TableSchema("TEMP_TABLE", attrs, true);
}

void JoinOperator::printRunningStats() const {
  cout << "# Result Tuples: " << numResultTuples << endl;
  cout << "# Used Buffer Pages: " << numUsedBufPages << endl;
  cout << "# I/Os: " << numIOs << endl;
}

vector<Attribute> JoinOperator::getCommonAttributes(
    const TableSchema& leftTableSchema,
    const TableSchema& rightTableSchema) const {
  vector<Attribute> common_attrs;
  for (int i = 0; i < rightTableSchema.getAttrCount(); ++i) {
    for (int j = 0; j < leftTableSchema.getAttrCount(); ++j) {
      if ((leftTableSchema.getAttrType(j) == rightTableSchema.getAttrType(i)) &&
          (leftTableSchema.getAttrName(j) == rightTableSchema.getAttrName(i))) {
        Attribute new_attr = Attribute(rightTableSchema.getAttrName(i),
                                       rightTableSchema.getAttrType(i),
                                       rightTableSchema.getAttrMaxSize(i),
                                       rightTableSchema.isAttrNotNull(i),
                                       rightTableSchema.isAttrUnique(i));
        common_attrs.push_back(new_attr);
      }
    }
  }
  return common_attrs;
}

/**
 * use the original key to generate the search key
 * @param key
 * @param common_attrs
 * @param TableSchema
 * @return
 */
string construct_search_key(string key,
                            vector<Attribute>& common_attrs,
                            const TableSchema& TableSchema) {
  string search_key;
  int current_index = 0;
  int current_attr_index = 0;
  for (int i = 0; i < TableSchema.getAttrCount(); ++i) {
    switch (TableSchema.getAttrType(i)) {
      case INT: {
        if (TableSchema.getAttrName(i) ==
                common_attrs[current_attr_index].attrName &&
            TableSchema.getAttrType(i) ==
                common_attrs[current_attr_index].attrType) {
          search_key += std::string(key, current_index, 4);
          current_attr_index++;
        }
        current_index += 4;
        break;
      }
      case CHAR: {
        int max_len = TableSchema.getAttrMaxSize(i);
        if (TableSchema.getAttrName(i) ==
                common_attrs[current_attr_index].attrName &&
            TableSchema.getAttrType(i) ==
                common_attrs[current_attr_index].attrType) {
          search_key += std::string(key, current_index, max_len);
          current_attr_index++;
        }
        current_index += max_len;
        current_index += (4 - (max_len % 4)) % 4;
        ;  // align to the multiple of 4
        break;
      }
      case VARCHAR: {
        int actual_len = key[current_index];
        current_index++;
        if (TableSchema.getAttrName(i) ==
                common_attrs[current_attr_index].attrName &&
            TableSchema.getAttrType(i) ==
                common_attrs[current_attr_index].attrType) {
          search_key += std::string(key, current_index, actual_len);
          current_attr_index++;
        }
        current_index += actual_len;
        current_index +=
            (4 - ((actual_len + 1) % 4)) % 4;  // align to the multiple of 4
        break;
      }
    }
    if (current_attr_index >= common_attrs.size())
      break;
  }
  return search_key;
}

string JoinOperator::joinTuples(string leftTuple,
                                string rightTuple,
                                const TableSchema& leftTableSchema,
                                const TableSchema& rightTableSchema) const {
  int cur_right_index = 0;  // current substring index in the right table key
  string result_tuple = leftTuple;

  for (int i = 0; i < rightTableSchema.getAttrCount(); ++i) {
    bool has_same = false;
    for (int j = 0; j < leftTableSchema.getAttrCount(); ++j) {
      if ((leftTableSchema.getAttrType(j) == rightTableSchema.getAttrType(i)) &&
          (leftTableSchema.getAttrName(j) == rightTableSchema.getAttrName(i))) {
        has_same = true;
      }
    }
    // if the key is only owned by right table, add it to the result tuple
    switch (rightTableSchema.getAttrType(i)) {
      case INT: {
        if (!has_same) {
          result_tuple += std::string(rightTuple, cur_right_index, 4);
        }
        cur_right_index += 4;
        break;
      }
      case CHAR: {
        int max_len = rightTableSchema.getAttrMaxSize(i);
        if (!has_same) {
          result_tuple += std::string(rightTuple, cur_right_index, max_len);
        }
        cur_right_index += max_len;
        unsigned align_ = (4 - (max_len % 4)) % 4;  // align to the multiple of
                                                    // 4
        for (int k = 0; k < align_; ++k) {
          result_tuple += "0";
          cur_right_index++;
        }
        break;
      }
      case VARCHAR: {
        int actual_len = rightTuple[cur_right_index];
        result_tuple += std::string(rightTuple, cur_right_index, 1);
        cur_right_index++;
        if (!has_same) {
          result_tuple += std::string(rightTuple, cur_right_index, actual_len);
        }
        cur_right_index += actual_len;
        unsigned align_ =
            (4 - ((actual_len + 1) % 4)) % 4;  // align to the multiple of 4
        for (int k = 0; k < align_; ++k) {
          result_tuple += "0";
          cur_right_index++;
        }
        break;
      }
    }
  }
  return result_tuple;
}

bool OnePassJoinOperator::execute(int numAvailableBufPages, File& resultFile) {
  if (isComplete)
    return true;

  numResultTuples = 0;
  numUsedBufPages = 0;
  numIOs = 0;

  // TODO: Execute the join algorithm

  isComplete = true;
  return true;
}

bool NestedLoopJoinOperator::execute(int numAvailableBufPages,
                                     File& resultFile) {
  if (isComplete)
    return true;

  numResultTuples = 0;
  numUsedBufPages = 0;
  numIOs = 0;

  // 寻找相同属性
  vector<Attribute> common_attrs = getCommonAttributes(leftTableSchema, rightTableSchema);
  vector<string> resTuples;
  badgerdb::FileIterator iter = leftTableFile.begin();
  bool left_flag = true;
  bool right_flag = true;
  while (iter != leftTableFile.end()) {
    // 每次将左关系的M-1个块读入缓冲池
    vector<badgerdb::Page*> in_buffer;
    for (int i = 0; i < numAvailableBufPages - 1; i++) {
      badgerdb::Page page = *iter;
      badgerdb::Page* buffered_page;
      bufMgr->readPage(&leftTableFile, page.page_number(), buffered_page);
      numIOs++;
      if (left_flag) {
        numUsedBufPages++;
      }
      in_buffer.push_back(buffered_page);
      iter++;
      if (iter == leftTableFile.end()) {
        break;
      }
    }
    left_flag = false;
    // 每次将右关系的1个块读入缓冲池
    for (badgerdb::FileIterator iter2 = rightTableFile.begin(); iter2 != rightTableFile.end(); iter2++) {
      badgerdb::Page page = *iter2;
      badgerdb::Page* rpage;
      bufMgr->readPage(&rightTableFile, page.page_number(), rpage);
      numIOs++;
      if (right_flag) {
        numUsedBufPages++;
        right_flag = false;
      }
      // 遍历右关系中的每一条元组
      for (badgerdb::PageIterator piter = rpage->begin(); piter != rpage->end(); piter++) {
        string rightKey = *piter;
        string search_key_right = construct_search_key(rightKey, common_attrs, rightTableSchema);
        // 遍历查找能与右关系元组进行连接的左关系元组
        for(int i = 0; i < in_buffer.size(); i++) {
          badgerdb::Page* lpage = in_buffer[i];
          for(badgerdb::PageIterator piter2 = lpage->begin(); piter2 != lpage->end(); piter2++) {
            string leftKey = *piter2;
            string search_key_left = construct_search_key(leftKey, common_attrs, leftTableSchema);
            // 相同属性相等则进行连接
            if(search_key_left == search_key_right) {
              string result_tuple = joinTuples(leftKey, rightKey, leftTableSchema, rightTableSchema);
              resTuples.push_back(result_tuple);
            }
          }
        }
      }
    }
  }
  
  // 将连接结果写入文件
  for(int i = 0; i < resTuples.size(); i++) {
    HeapFileManager::insertTuple(resTuples[i], resultFile, bufMgr);
  }
  numResultTuples = resTuples.size();

  isComplete = true;
  return true;
}

BucketId GraceHashJoinOperator::hash(const string& key) const {
  std::hash<string> strHash;
  return strHash(key) % numBuckets;
}

bool GraceHashJoinOperator::execute(int numAvailableBufPages,
                                    File& resultFile) {
  if (isComplete)
    return true;

  numResultTuples = 0;
  numUsedBufPages = 0;
  numIOs = 0;

  // TODO: Execute the join algorithm
  
  isComplete = true;
  return true;
}

}  // namespace badgerdb
