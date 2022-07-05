/**
 * @author See Contributors.txt for code contributors and overview of BadgerDB.
 *
 * @section LICENSE
 * Copyright (c) 2012 Database Group, Computer Sciences Department, University of Wisconsin-Madison.
 */

#include <memory>
#include <iostream>
#include "buffer.h"
#include "exceptions/buffer_exceeded_exception.h"
#include "exceptions/page_not_pinned_exception.h"
#include "exceptions/page_pinned_exception.h"
#include "exceptions/bad_buffer_exception.h"
#include "exceptions/hash_not_found_exception.h"

namespace badgerdb { 

BufMgr::BufMgr(std::uint32_t bufs)
	: numBufs(bufs) {
  bufDescTable = new BufDesc[bufs];

  for (FrameId i = 0; i < bufs; i++) 
  {
    bufDescTable[i].frameNo = i;
    bufDescTable[i].valid = false;
  }

  bufPool = new Page[bufs];

  int htsize = ((((int) (bufs * 1.2))*2)/2)+1;
  hashTable = new BufHashTbl (htsize);  // allocate the buffer hash table

  clockHand = bufs - 1;
}


BufMgr::~BufMgr() {
  for (FrameId i = 0; i < numBufs; i++) 
  {
    if (bufDescTable[i].dirty)
    {
      bufDescTable[i].file->writePage(bufPool[i]);  // write back the dirty pages to disk
    }
  }
  
  delete[] bufPool;
  delete[] bufDescTable;
  delete hashTable; 
}

void BufMgr::advanceClock()
{
  clockHand++;
  clockHand %= numBufs;
}

void BufMgr::allocBuf(FrameId & frame) 
{
  unsigned pinned_count = 0;  // the number of pinned pages
  
  while (true)
  {
    advanceClock();
    
    if (!bufDescTable[clockHand].valid)  // an invalid page, use it directly
    {
      frame = clockHand;
      return;
    }
    
    if (bufDescTable[clockHand].refbit)  // a page with  true refbit
    {
      bufDescTable[clockHand].refbit = false;
      continue;
    }
    
    if (bufDescTable[clockHand].pinCnt)  // a pinned page 
    {
      pinned_count++;
      
      if (pinned_count == numBufs)
        throw BufferExceededException();  // all pages are pinned, throw an exception
      else
        continue;
    }
    
    if (bufDescTable[clockHand].dirty)  // a dirty page
    {
      bufDescTable[clockHand].file->writePage(bufPool[clockHand]);  // write back to disk
      bufDescTable[clockHand].dirty = false;
    }
    
    try
    {
      hashTable->remove(bufDescTable[clockHand].file, bufDescTable[clockHand].pageNo);  // a valid page, remove it from hash table
    }
    catch (HashNotFoundException &)
    {
    }
    frame = clockHand;
    
    break;
  }
}

	
void BufMgr::readPage(File* file, const PageId pageNo, Page*& page)
{
  FrameId frame;
  try
  {
    hashTable->lookup(file, pageNo, frame);
    
    // page in the buffer pool
    bufDescTable[frame].refbit = true;
    bufDescTable[frame].pinCnt++;
    page = bufPool + frame;
  }
  catch (HashNotFoundException &)  // page not in the buffer pool
  {
    allocBuf(frame);
    bufPool[frame] = file->readPage(pageNo);
    hashTable->insert(file, pageNo, frame);
    bufDescTable[frame].Set(file, pageNo);
    page = bufPool + frame;
  }
}


void BufMgr::unPinPage(File* file, const PageId pageNo, const bool dirty) 
{
  FrameId frame;
  try
  {
    hashTable->lookup(file, pageNo, frame);
  }
  catch (HashNotFoundException &)
  {
    // the page is not in the buffer pool, do nothing
    return;
  }
  
  if (bufDescTable[frame].pinCnt > 0)
  {
    bufDescTable[frame].pinCnt--;
    if (dirty)
      bufDescTable[frame].dirty = true;
  }
  else
  {
    throw PageNotPinnedException(bufDescTable[frame].file->filename(), bufDescTable[frame].pageNo, frame);
  }
}

void BufMgr::flushFile(const File* file) 
{
  for (FrameId fi = 0; fi < numBufs; fi++)
  {
    if (bufDescTable[fi].file == file)
    {
      if (!bufDescTable[fi].valid)  // invalid page
        throw BadBufferException(fi, bufDescTable[fi].dirty, bufDescTable[fi].valid, bufDescTable[fi].refbit);
      
      if (bufDescTable[fi].pinCnt > 0)  // pinned page
        throw PagePinnedException(file->filename(), bufDescTable[fi].pageNo, fi);
      
      if (bufDescTable[fi].dirty)  // dirty page
      {
        bufDescTable[fi].file->writePage(bufPool[fi]);
        bufDescTable[fi].dirty = false;
      }

      hashTable->remove(file, bufDescTable[fi].pageNo);
      bufDescTable[fi].Clear();
    }
  }
}

void BufMgr::allocPage(File* file, PageId &pageNo, Page*& page) 
{
  FrameId frame;
  
  Page p = file->allocatePage();  // allocate a page
  allocBuf(frame);  // allocate a frame
  
  bufPool[frame] = p;
  pageNo = p.page_number();
  
  hashTable->insert(file, pageNo, frame);
  bufDescTable[frame].Set(file, pageNo);  
  
  page = bufPool + frame;
}

void BufMgr::disposePage(File* file, const PageId PageNo)
{
  FrameId frame;
  try
  {
    hashTable->lookup(file, PageNo, frame);
    
    // page in the buffer pool
    bufDescTable[frame].Clear();
    hashTable->remove(file, PageNo);
  }
  catch (HashNotFoundException &)
  {
    // page not in the buffer pool, do nothing
  }
  
  file->deletePage(PageNo);
}

void BufMgr::printSelf(void) 
{
  BufDesc* tmpbuf;
  int validFrames = 0;
  
  for (std::uint32_t i = 0; i < numBufs; i++)
  {
    tmpbuf = &(bufDescTable[i]);
    std::cout << "FrameNo:" << i << " ";
    tmpbuf->Print();

    if (tmpbuf->valid == true)
    validFrames++;
  }

  std::cout << "Total Number of Valid Frames:" << validFrames << "\n";
}

}
