import pymysql.cursors


def init_dept_name(cursor, conn):
    sql = "INSERT INTO Department VALUES (%s, NULL, NULL);"
    dname = 'Math'
    cursor.execute(sql, dname)
    dname = 'Physics'
    cursor.execute(sql, dname)
    dname = 'CS'
    cursor.execute(sql, dname)
    dname = 'AI'
    cursor.execute(sql, dname)
    conn.commit()


def init_teacher(cursor, conn):
    sql = "INSERT INTO Teacher VALUES (%s, %s, %s, %s, %s, %s);"
    tno = 'T-00000001'
    tname = 'Gauss'
    tsex = 'M'
    tage = 48
    tworkyears = 20
    tdept = 'Math'
    cursor.execute(sql, (tno, tname, tsex, tage, tworkyears, tdept))
    tno = 'T-00000002'
    tname = 'Newton'
    tage = 50
    tworkyears = 25
    tdept = 'Physics'
    cursor.execute(sql, (tno, tname, tsex, tage, tworkyears, tdept))
    tno = 'T-00000003'
    tname = 'Turing'
    tage = 39
    tworkyears = 17
    tdept = 'CS'
    cursor.execute(sql, (tno, tname, tsex, tage, tworkyears, tdept))
    for num in range(4, 21):
        tno = 'T-' + str('%08d' % num)
        tname = 'T' + str(num)
        tsex = 'F' if num % 3 == 1 else 'M'
        tage = num + 25
        tworkyears = num
        if num % 4 == 0:
            tdept = 'Math'
        elif num % 4 == 1:
            tdept = 'Physics'
        elif num % 4 == 2:
            tdept = 'CS'
        else:
            tdept = 'AI'
        cursor.execute(sql, (tno, tname, tsex, tage, tworkyears, tdept))
    conn.commit()


def init_dept_leader(cursor, conn):
    sql = "UPDATE Department SET DLno = 'T-00000001', DLname = 'Gauss' WHERE Dname = 'Math';"
    cursor.execute(sql)
    sql = "UPDATE Department SET DLno = 'T-00000002', DLname = 'Newton' WHERE Dname = 'Physics';"
    cursor.execute(sql)
    sql = "UPDATE Department SET DLno = 'T-00000003', DLname = 'Turing' WHERE Dname = 'CS';"
    cursor.execute(sql)
    sql = "UPDATE Department SET DLno = 'T-00000003', DLname = 'Turing' WHERE Dname = 'AI';"
    cursor.execute(sql)
    conn.commit()


def init_student(cursor, conn, sdept, total_num):
    sql = "INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s);"
    for num in range(1, total_num + 1):
        if sdept == 'Math':
            sno = 'MA-' + str('%07d' % num)
        elif sdept == 'Physics':
            sno = 'PH-' + str('%07d' % num)
        elif sdept == 'CS':
            sno = 'CS-' + str('%07d' % num)
        else:
            sno = 'AI-' + str('%07d' % num)
        sname = 'S' + str('%07d' % num)
        ssex = 'F' if num % 4 == 1 else 'M'
        if num <= total_num / 4:
            sage = 21
            sgrade = 4
        elif num <= 2 * total_num / 4:
            sage = 20
            sgrade = 3
        elif num <= 3 * total_num / 4:
            sage = 19
            sgrade = 2
        else:
            sage = 18
            sgrade = 1
        cursor.execute(sql, (sno, sname, ssex, sage, sgrade, sdept))
    conn.commit()


def init_classroom(cursor, conn, total_num):
    sql = "INSERT INTO Classroom VALUES (%s, %s, %s);"
    for num in range(1, total_num + 1):
        rno = 'R-' + str('%03d' % num)
        if num <= total_num / 3:
            rbuilding = 1
            rcapacity = 100
        elif num <= 2 * total_num / 3:
            rbuilding = 2
            rcapacity = 200
        else:
            rbuilding = 3
            rcapacity = 300
        cursor.execute(sql, (rno, rbuilding, rcapacity))
    conn.commit()


def init_course(cursor, conn, total_num, room_num):
    sql = "INSERT INTO Course VALUES (%s, %s, %s, %s);"
    for num in range(1, total_num + 1):
        cno = 'C-' + str('%03d' % num)
        cname = 'C' + str('%07d' % num)
        ccredit = 2 if num < total_num / 2 else 3
        croom = 'R-' + str('%03d' % (num % room_num))
        cursor.execute(sql, (cno, cname, ccredit, croom))
    conn.commit()


def init_project(cursor, conn, total_num):
    sql = "INSERT INTO Project VALUES (%s, %s);"
    for num in range(1, total_num + 1):
        pname = 'P' + str(num)
        plno = 'T-' + str('%08d' % (num % 20)) if num % 20 != 0 else 'T-' + str('%08d' % 20)
        cursor.execute(sql, (pname, plno))
    conn.commit()


def init_sc(cursor, conn, course_num, student_dept, student_num):
    sql = "INSERT INTO SC VALUES (%s, %s, %s);"
    for num in range(1, course_num + 1):
        cno = 'C-' + str('%03d' % num)
        for i in range(1, student_num + 1):
            if i % int(2 * course_num / 3) == num:
                if student_dept == 'Math':
                    sno = 'MA-' + str('%07d' % i)
                elif student_dept == 'Physics':
                    sno = 'PH-' + str('%07d' % i)
                elif student_dept == 'CS':
                    sno = 'CS-' + str('%07d' % i)
                else:
                    sno = 'AI-' + str('%07d' % i)
                grade = 90 + (i % 10)
                cursor.execute(sql, (sno, cno, grade))
    conn.commit()


def init_tc(cursor, conn, course_num):
    sql = "INSERT INTO TC VALUES (%s, %s, %s);"
    for num in range(1, course_num + 1):
        cno = 'C-' + str('%03d' % num)
        tno = 'T-' + str('%08d' % (num % 20)) if num % 20 != 0 else 'T-' + str('%08d' % 20)
        hours = 24
        cursor.execute(sql, (tno, cno, hours))
        if num > course_num / 2:
            tno = 'T-' + str('%08d' % ((num + 1) % 20)) if (num + 1) % 20 != 0 else 'T-' + str('%08d' % 20)
            hours = 12
            cursor.execute(sql, (tno, cno, hours))
    conn.commit()


def init_pp(cursor, conn, project_num):
    sql = "INSERT INTO PP VALUES (%s, %s);"
    for num in range(1, project_num + 1):
        pname = 'P' + str(num)
        tno = 'T-' + str('%08d' % ((num + 1) % 20)) if (num + 1) % 20 != 0 else 'T-' + str('%08d' % 20)
        cursor.execute(sql, (tno, pname))
        tno = 'T-' + str('%08d' % ((num + 2) % 20)) if (num + 2) % 20 != 0 else 'T-' + str('%08d' % 20)
        cursor.execute(sql, (tno, pname))
    conn.commit()


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()

    # 创建院系
    init_dept_name(cursor, conn)
    # 录入教师信息
    init_teacher(cursor, conn)
    # 录入各院系系主任
    init_dept_leader(cursor, conn)
    # 录入学生信息
    init_student(cursor, conn, 'Math', 1200)
    init_student(cursor, conn, 'Physics', 1000)
    init_student(cursor, conn, 'CS', 2000)
    init_student(cursor, conn, 'AI', 1600)
    # 录入教室信息
    init_classroom(cursor, conn, 30)
    # 录入课程信息
    init_course(cursor, conn, 15, 30)
    # 录入科研项目信息
    init_project(cursor, conn, 10)
    # 录入选课信息
    init_sc(cursor, conn, 15, 'Math', 1200)
    init_sc(cursor, conn, 15, 'Physics', 1000)
    init_sc(cursor, conn, 15, 'CS', 2000)
    init_sc(cursor, conn, 15, 'AI', 1600)
    # 录入授课信息
    init_tc(cursor, conn, 15)
    # 录入参与科研信息
    init_pp(cursor, conn, 10)

    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
