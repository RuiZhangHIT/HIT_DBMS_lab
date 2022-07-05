import pymysql.cursors
from tkinter import *
import time


def search_department():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Department"
    cond = False
    if len(str(dname.get())) != 0:
        sql += ' WHERE Dname = \'' + str(dname.get()) + '\''
        cond = True
    if len(str(dlno.get())) != 0:
        if cond:
            sql += ' AND DLno = \'' + str(dlno.get()) + '\''
        else:
            sql += ' WHERE DLno = \'' + str(dlno.get()) + '\''
            cond = True
    if len(str(dlname.get())) != 0:
        if cond:
            sql += ' AND DLname = \'' + str(dlname.get()) + '\''
        else:
            sql += ' WHERE DLname = \'' + str(dlname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Department')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Dname DLno DLname\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_department():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Department VALUES ("
    if len(str(dname.get())) != 0:
        sql += '\'' + str(dname.get()) + '\', '
    else:
        sql += 'NULL, '
    if len(str(dlno.get())) != 0:
        sql += '\'' + str(dlno.get()) + '\', '
    else:
        sql += 'NULL, '
    if len(str(dlname.get())) != 0:
        sql += '\'' + str(dlname.get()) + '\');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Department')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_department():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Department"
    cond = False
    if len(str(dname.get())) != 0:
        sql += ' WHERE Dname = \'' + str(dname.get()) + '\''
        cond = True
    if len(str(dlno.get())) != 0:
        if cond:
            sql += ' AND DLno = \'' + str(dlno.get()) + '\''
        else:
            sql += ' WHERE DLno = \'' + str(dlno.get()) + '\''
            cond = True
    if len(str(dlname.get())) != 0:
        if cond:
            sql += ' AND DLname = \'' + str(dlname.get()) + '\''
        else:
            sql += ' WHERE DLname = \'' + str(dlname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Department')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_teacher():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Teacher"
    cond = False
    if len(str(tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(tno.get()) + '\''
        cond = True
    if len(str(tname.get())) != 0:
        if cond:
            sql += ' AND Tname = \'' + str(tname.get()) + '\''
        else:
            sql += ' WHERE Tname = \'' + str(tname.get()) + '\''
            cond = True
    if len(str(tsex.get())) != 0:
        if cond:
            sql += ' AND Tsex = \'' + str(tsex.get()) + '\''
        else:
            sql += ' WHERE Tsex = \'' + str(tsex.get()) + '\''
            cond = True
    if len(str(tage.get())) != 0:
        if cond:
            sql += ' AND Tage = ' + str(tage.get())
        else:
            sql += ' WHERE Tage = ' + str(tage.get())
            cond = True
    if len(str(tworkyears.get())) != 0:
        if cond:
            sql += ' AND Tworkyears = ' + str(tworkyears.get())
        else:
            sql += ' WHERE Tworkyears = ' + str(tworkyears.get())
            cond = True
    if len(str(tdept.get())) != 0:
        if cond:
            sql += ' AND Tdept = \'' + str(tdept.get()) + '\''
        else:
            sql += ' WHERE Tdept = \'' + str(tdept.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Teacher')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Tno Tname Tsex Tage Tworkyears Tdept\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_teacher():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Teacher VALUES ("
    if len(str(tno.get())) != 0:
        sql += '\'' + str(tno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(tname.get())) != 0:
        sql += '\'' + str(tname.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(tsex.get())) != 0:
        sql += '\'' + str(tsex.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(tage.get())) != 0:
        sql += str(tage.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(tworkyears.get())) != 0:
        sql += str(tworkyears.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(tdept.get())) != 0:
        sql += '\'' + str(tdept.get()) + '\');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Teacher')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_teacher():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Teacher"
    cond = False
    if len(str(tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(tno.get()) + '\''
        cond = True
    if len(str(tname.get())) != 0:
        if cond:
            sql += ' AND Tname = \'' + str(tname.get()) + '\''
        else:
            sql += ' WHERE Tname = \'' + str(tname.get()) + '\''
            cond = True
    if len(str(tsex.get())) != 0:
        if cond:
            sql += ' AND Tsex = \'' + str(tsex.get()) + '\''
        else:
            sql += ' WHERE Tsex = \'' + str(tsex.get()) + '\''
            cond = True
    if len(str(tage.get())) != 0:
        if cond:
            sql += ' AND Tage = ' + str(tage.get())
        else:
            sql += ' WHERE Tage = ' + str(tage.get())
            cond = True
    if len(str(tworkyears.get())) != 0:
        if cond:
            sql += ' AND Tworkyears = ' + str(tworkyears.get())
        else:
            sql += ' WHERE Tworkyears = ' + str(tworkyears.get())
            cond = True
    if len(str(tdept.get())) != 0:
        if cond:
            sql += ' AND Tdept = \'' + str(tdept.get()) + '\''
        else:
            sql += ' WHERE Tdept = \'' + str(tdept.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Teacher')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_student():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Student"
    cond = False
    if len(str(sno.get())) != 0:
        sql += ' WHERE Sno = \'' + str(sno.get()) + '\''
        cond = True
    if len(str(sname.get())) != 0:
        if cond:
            sql += ' AND Sname = \'' + str(sname.get()) + '\''
        else:
            sql += ' WHERE Sname = \'' + str(sname.get()) + '\''
            cond = True
    if len(str(ssex.get())) != 0:
        if cond:
            sql += ' AND Ssex = \'' + str(ssex.get()) + '\''
        else:
            sql += ' WHERE Ssex = \'' + str(ssex.get()) + '\''
            cond = True
    if len(str(sage.get())) != 0:
        if cond:
            sql += ' AND Sage = ' + str(sage.get())
        else:
            sql += ' WHERE Sage = ' + str(sage.get())
            cond = True
    if len(str(sgrade.get())) != 0:
        if cond:
            sql += ' AND Sgrade = ' + str(sgrade.get())
        else:
            sql += ' WHERE Sgrade = ' + str(sgrade.get())
            cond = True
    if len(str(sdept.get())) != 0:
        if cond:
            sql += ' AND Sdept = \'' + str(sdept.get()) + '\''
        else:
            sql += ' WHERE Sdept = \'' + str(sdept.get()) + '\''
    print(sql)
    start_time = time.time()
    cursor.execute(sql)
    end_time = time.time()
    print('search time: ' + str(end_time - start_time) + 's')
    top = Tk()
    top.title('Student')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Sno Sname Ssex Sage Sgrade Sdept\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_student():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Student VALUES ("
    if len(str(sno.get())) != 0:
        sql += '\'' + str(sno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(sname.get())) != 0:
        sql += '\'' + str(sname.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(ssex.get())) != 0:
        sql += '\'' + str(ssex.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(sage.get())) != 0:
        sql += str(sage.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(sgrade.get())) != 0:
        sql += str(sgrade.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(sdept.get())) != 0:
        sql += '\'' + str(sdept.get()) + '\');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Student')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_student():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Student"
    cond = False
    if len(str(sno.get())) != 0:
        sql += ' WHERE Sno = \'' + str(sno.get()) + '\''
        cond = True
    if len(str(sname.get())) != 0:
        if cond:
            sql += ' AND Sname = \'' + str(sname.get()) + '\''
        else:
            sql += ' WHERE Sname = \'' + str(sname.get()) + '\''
            cond = True
    if len(str(ssex.get())) != 0:
        if cond:
            sql += ' AND Ssex = \'' + str(ssex.get()) + '\''
        else:
            sql += ' WHERE Ssex = \'' + str(ssex.get()) + '\''
            cond = True
    if len(str(sage.get())) != 0:
        if cond:
            sql += ' AND Sage = ' + str(sage.get())
        else:
            sql += ' WHERE Sage = ' + str(sage.get())
            cond = True
    if len(str(sgrade.get())) != 0:
        if cond:
            sql += ' AND Sgrade = ' + str(sgrade.get())
        else:
            sql += ' WHERE Sgrade = ' + str(sgrade.get())
            cond = True
    if len(str(sdept.get())) != 0:
        if cond:
            sql += ' AND Sdept = \'' + str(sdept.get()) + '\''
        else:
            sql += ' WHERE Sdept = \'' + str(sdept.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Student')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_course():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Course"
    cond = False
    if len(str(cno.get())) != 0:
        sql += ' WHERE Cno = \'' + str(cno.get()) + '\''
        cond = True
    if len(str(cname.get())) != 0:
        if cond:
            sql += ' AND Cname = \'' + str(cname.get()) + '\''
        else:
            sql += ' WHERE Cname = \'' + str(cname.get()) + '\''
            cond = True
    if len(str(ccredit.get())) != 0:
        if cond:
            sql += ' AND Ccredit = ' + str(ccredit.get())
        else:
            sql += ' WHERE Ccredit = ' + str(ccredit.get())
            cond = True
    if len(str(croom.get())) != 0:
        if cond:
            sql += ' AND Croom = \'' + str(croom.get()) + '\''
        else:
            sql += ' WHERE Croom = \'' + str(croom.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Course')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Cno Cname Ccredit Croom\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_course():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Course VALUES ("
    if len(str(cno.get())) != 0:
        sql += '\'' + str(cno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(cname.get())) != 0:
        sql += '\'' + str(cname.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(ccredit.get())) != 0:
        sql += str(ccredit.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(croom.get())) != 0:
        sql += '\'' + str(croom.get()) + '\');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Course')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_course():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Course"
    cond = False
    if len(str(cno.get())) != 0:
        sql += ' WHERE Cno = \'' + str(cno.get()) + '\''
        cond = True
    if len(str(cname.get())) != 0:
        if cond:
            sql += ' AND Cname = \'' + str(cname.get()) + '\''
        else:
            sql += ' WHERE Cname = \'' + str(cname.get()) + '\''
            cond = True
    if len(str(ccredit.get())) != 0:
        if cond:
            sql += ' AND Ccredit = ' + str(ccredit.get())
        else:
            sql += ' WHERE Ccredit = ' + str(ccredit.get())
            cond = True
    if len(str(croom.get())) != 0:
        if cond:
            sql += ' AND Croom = \'' + str(croom.get()) + '\''
        else:
            sql += ' WHERE Croom = \'' + str(croom.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Course')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_project():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Project"
    cond = False
    if len(str(pname.get())) != 0:
        sql += ' WHERE Pname = \'' + str(pname.get()) + '\''
        cond = True
    if len(str(plno.get())) != 0:
        if cond:
            sql += ' AND PLno = \'' + str(plno.get()) + '\''
        else:
            sql += ' WHERE PLno = \'' + str(plno.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Project')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Pname PLno\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_project():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Project VALUES ("
    if len(str(pname.get())) != 0:
        sql += '\'' + str(pname.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(plno.get())) != 0:
        sql += '\'' + str(plno.get()) + '\');'
    else:
        sql += 'NULL); '
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Project')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_project():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Project"
    cond = False
    if len(str(pname.get())) != 0:
        sql += ' WHERE Pname = \'' + str(pname.get()) + '\''
        cond = True
    if len(str(plno.get())) != 0:
        if cond:
            sql += ' AND PLno = \'' + str(plno.get()) + '\''
        else:
            sql += ' WHERE PLno = \'' + str(plno.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Project')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_classroom():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Classroom"
    cond = False
    if len(str(rno.get())) != 0:
        sql += ' WHERE Rno = \'' + str(rno.get()) + '\''
        cond = True
    if len(str(rbuilding.get())) != 0:
        if cond:
            sql += ' AND Rbuilding = ' + str(rbuilding.get())
        else:
            sql += ' WHERE Rbuilding = ' + str(rbuilding.get())
            cond = True
    if len(str(rcapacity.get())) != 0:
        if cond:
            sql += ' AND Rcapacity = ' + str(rcapacity.get())
        else:
            sql += ' WHERE Rcapacity = ' + str(rcapacity.get())
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Classroom')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Rno Rbuilding Rcapacity\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_classroom():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO Classroom VALUES ("
    if len(str(rno.get())) != 0:
        sql += '\'' + str(rno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(rbuilding.get())) != 0:
        sql += str(rbuilding.get()) + ','
    else:
        sql += 'NULL, '
    if len(str(rcapacity.get())) != 0:
        sql += str(rcapacity.get()) + ');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Classroom')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_classroom():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM Classroom"
    cond = False
    if len(str(rno.get())) != 0:
        sql += ' WHERE Rno = \'' + str(rno.get()) + '\''
        cond = True
    if len(str(rbuilding.get())) != 0:
        if cond:
            sql += ' AND Rbuilding = ' + str(rbuilding.get())
        else:
            sql += ' WHERE Rbuilding = ' + str(rbuilding.get())
            cond = True
    if len(str(rcapacity.get())) != 0:
        if cond:
            sql += ' AND Rcapacity = ' + str(rcapacity.get())
        else:
            sql += ' WHERE Rcapacity = ' + str(rcapacity.get())
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('Classroom')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_sc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM SC"
    cond = False
    if len(str(sc_sno.get())) != 0:
        sql += ' WHERE Sno = \'' + str(sc_sno.get()) + '\''
        cond = True
    if len(str(sc_cno.get())) != 0:
        if cond:
            sql += ' AND Cno = \'' + str(sc_cno.get()) + '\''
        else:
            sql += ' WHERE Cno = \'' + str(sc_cno.get()) + '\''
            cond = True
    if len(str(grade.get())) != 0:
        if cond:
            sql += ' AND Grade = ' + str(grade.get())
        else:
            sql += ' WHERE Grade = ' + str(grade.get())
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('SC')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Sno Cno Grade\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_sc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO SC VALUES("
    if len(str(sc_sno.get())) != 0:
        sql += '\'' + str(sc_sno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(sc_cno.get())) != 0:
        sql += '\'' + str(sc_cno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(grade.get())) != 0:
        sql += str(grade.get()) + ');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('SC')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_sc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM SC"
    cond = False
    if len(str(sc_sno.get())) != 0:
        sql += ' WHERE Sno = \'' + str(sc_sno.get()) + '\''
        cond = True
    if len(str(sc_cno.get())) != 0:
        if cond:
            sql += ' AND Cno = \'' + str(sc_cno.get()) + '\''
        else:
            sql += ' WHERE Cno = \'' + str(sc_cno.get()) + '\''
            cond = True
    if len(str(grade.get())) != 0:
        if cond:
            sql += ' AND Grade = ' + str(grade.get())
        else:
            sql += ' WHERE Grade = ' + str(grade.get())
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('SC')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_tc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM TC"
    cond = False
    if len(str(tc_tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(tc_tno.get()) + '\''
        cond = True
    if len(str(tc_cno.get())) != 0:
        if cond:
            sql += ' AND Cno = \'' + str(tc_cno.get()) + '\''
        else:
            sql += ' WHERE Cno = \'' + str(tc_cno.get()) + '\''
            cond = True
    if len(str(hours.get())) != 0:
        if cond:
            sql += ' AND Hours = ' + str(hours.get())
        else:
            sql += ' WHERE Hours = ' + str(hours.get())
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('TC')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Tno Cno Hours\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_tc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO TC VALUES("
    if len(str(tc_tno.get())) != 0:
        sql += '\'' + str(tc_tno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(tc_cno.get())) != 0:
        sql += '\'' + str(tc_cno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(hours.get())) != 0:
        sql += str(hours.get()) + ');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('TC')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_tc():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM TC"
    cond = False
    if len(str(tc_tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(tc_tno.get()) + '\''
        cond = True
    if len(str(tc_cno.get())) != 0:
        if cond:
            sql += ' AND Cno = \'' + str(tc_cno.get()) + '\''
        else:
            sql += ' WHERE Cno = \'' + str(tc_cno.get()) + '\''
            cond = True
    if len(str(hours.get())) != 0:
        if cond:
            sql += ' AND Hours = ' + str(hours.get())
        else:
            sql += ' WHERE Hours = ' + str(hours.get())
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('TC')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def search_pp():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM PP"
    cond = False
    if len(str(pp_tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(pp_tno.get()) + '\''
        cond = True
    if len(str(pp_pname.get())) != 0:
        if cond:
            sql += ' AND Pname = \'' + str(pp_pname.get()) + '\''
        else:
            sql += ' WHERE Pname = \'' + str(pp_pname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('PP')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Tno Pname\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def insert_pp():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO PP VALUES("
    if len(str(pp_tno.get())) != 0:
        sql += '\'' + str(pp_tno.get()) + '\','
    else:
        sql += 'NULL, '
    if len(str(pp_pname.get())) != 0:
        sql += '\'' + str(pp_pname.get()) + '\');'
    else:
        sql += 'NULL);'
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('PP')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully inserted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def delete_pp():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "DELETE FROM PP"
    cond = False
    if len(str(pp_tno.get())) != 0:
        sql += ' WHERE Tno = \'' + str(pp_tno.get()) + '\''
        cond = True
    if len(str(pp_pname.get())) != 0:
        if cond:
            sql += ' AND Pname = \'' + str(pp_pname.get()) + '\''
        else:
            sql += ' WHERE Pname = \'' + str(pp_pname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    conn.commit()
    top = Tk()
    top.title('PP')
    top.geometry("500x50+300+300")
    Label(top, text='Successfully deleted data!', font=('Times New Roman', 10, 'bold')).pack()
    cursor.close()
    conn.close()


def pt_leader():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Project_Leader"
    cond = False
    if len(str(pt_pname.get())) != 0:
        sql += ' WHERE Pname = \'' + str(pt_pname.get()) + '\''
        cond = True
    if len(str(pt_tname.get())) != 0:
        if cond:
            sql += ' AND Tname = \'' + str(pt_tname.get()) + '\''
        else:
            sql += ' WHERE Tname = \'' + str(pt_tname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Project_Leader')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Pname Tname\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


def pt_participant():
    conn = pymysql.connect(host='localhost', user='root', password='Zr200126', db='school', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT * FROM Project_Teacher"
    cond = False
    if len(str(pt_pname.get())) != 0:
        sql += ' WHERE Pname = \'' + str(pt_pname.get()) + '\''
        cond = True
    if len(str(pt_tname.get())) != 0:
        if cond:
            sql += ' AND Tname = \'' + str(pt_tname.get()) + '\''
        else:
            sql += ' WHERE Tname = \'' + str(pt_tname.get()) + '\''
    print(sql)
    cursor.execute(sql)
    top = Tk()
    top.title('Project_Participant')
    top.geometry("500x500+100+100")
    sbar = Scrollbar(top)
    sbar.pack(side=RIGHT, fill=Y)
    text = Text(top, yscrollcommand=sbar.set)
    text.insert(END, 'Pname Tname\n')
    for i in cursor.fetchall():
        print(i)
        text.insert(END, str(i) + '\n')
    text.pack(side=LEFT, fill=BOTH)
    sbar.config(command=text.yview)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    root = Tk()
    root.title('School Database')
    root.geometry('800x620+300+150')
    Label(root, text='SCHOOL', font=('Times New Roman', 30, 'bold')).pack()

    root_frame = Frame(root)
    root_frame.pack()

    dept_frame = Frame(root_frame)
    Label(dept_frame, text='Department', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(dept_frame, text='Dname：').grid(row=1)
    Label(dept_frame, text='DLno：').grid(row=2)
    Label(dept_frame, text='DLname：').grid(row=3)
    entry1 = Entry(dept_frame)
    entry1.grid(row=1, column=2)
    dname = StringVar()
    entry1["textvariable"] = dname
    entry2 = Entry(dept_frame)
    entry2.grid(row=2, column=2)
    dlno = StringVar()
    entry2["textvariable"] = dlno
    entry3 = Entry(dept_frame)
    entry3.grid(row=3, column=2)
    dlname = StringVar()
    entry3["textvariable"] = dlname
    Button(dept_frame, text='delete', command=delete_department).grid(row=4, column=0)
    Button(dept_frame, text='insert', command=insert_department).grid(row=4, column=1)
    Button(dept_frame, text='search', command=search_department).grid(row=4, column=2)
    dept_frame.grid(row=0, column=0)

    teacher_frame = Frame(root_frame)
    Label(teacher_frame, text='Teacher', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(teacher_frame, text='Tno：').grid(row=1)
    Label(teacher_frame, text='Tname：').grid(row=2)
    Label(teacher_frame, text='Tsex：').grid(row=3)
    Label(teacher_frame, text='Tage：').grid(row=4)
    Label(teacher_frame, text='Tworkyears：').grid(row=5)
    Label(teacher_frame, text='Tdept：').grid(row=6)
    entry1 = Entry(teacher_frame)
    entry1.grid(row=1, column=2)
    tno = StringVar()
    entry1["textvariable"] = tno
    entry2 = Entry(teacher_frame)
    entry2.grid(row=2, column=2)
    tname = StringVar()
    entry2["textvariable"] = tname
    entry3 = Entry(teacher_frame)
    entry3.grid(row=3, column=2)
    tsex = StringVar()
    entry3["textvariable"] = tsex
    entry4 = Entry(teacher_frame)
    entry4.grid(row=4, column=2)
    tage = StringVar()
    entry4["textvariable"] = tage
    entry5 = Entry(teacher_frame)
    entry5.grid(row=5, column=2)
    tworkyears = StringVar()
    entry5["textvariable"] = tworkyears
    entry6 = Entry(teacher_frame)
    entry6.grid(row=6, column=2)
    tdept = StringVar()
    entry6["textvariable"] = tdept
    Button(teacher_frame, text='delete', command=delete_teacher).grid(row=7, column=0)
    Button(teacher_frame, text='insert', command=insert_teacher).grid(row=7, column=1)
    Button(teacher_frame, text='search', command=search_teacher).grid(row=7, column=2)
    teacher_frame.grid(row=0, column=1)

    student_frame = Frame(root_frame)
    Label(student_frame, text='Student', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(student_frame, text='Sno：').grid(row=1)
    Label(student_frame, text='Sname：').grid(row=2)
    Label(student_frame, text='Ssex：').grid(row=3)
    Label(student_frame, text='Sage：').grid(row=4)
    Label(student_frame, text='Sgrade：').grid(row=5)
    Label(student_frame, text='Sdept：').grid(row=6)
    entry1 = Entry(student_frame)
    entry1.grid(row=1, column=2)
    sno = StringVar()
    entry1["textvariable"] = sno
    entry2 = Entry(student_frame)
    entry2.grid(row=2, column=2)
    sname = StringVar()
    entry2["textvariable"] = sname
    entry3 = Entry(student_frame)
    entry3.grid(row=3, column=2)
    ssex = StringVar()
    entry3["textvariable"] = ssex
    entry4 = Entry(student_frame)
    entry4.grid(row=4, column=2)
    sage = StringVar()
    entry4["textvariable"] = sage
    entry5 = Entry(student_frame)
    entry5.grid(row=5, column=2)
    sgrade = StringVar()
    entry5["textvariable"] = sgrade
    entry6 = Entry(student_frame)
    entry6.grid(row=6, column=2)
    sdept = StringVar()
    entry6["textvariable"] = sdept
    Button(student_frame, text='delete', command=delete_student).grid(row=7, column=0)
    Button(student_frame, text='insert', command=insert_student).grid(row=7, column=1)
    Button(student_frame, text='search', command=search_student).grid(row=7, column=2)
    student_frame.grid(row=0, column=2)

    course_frame = Frame(root_frame)
    Label(course_frame, text='Course', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(course_frame, text='Cno：').grid(row=1)
    Label(course_frame, text='Cname：').grid(row=2)
    Label(course_frame, text='Ccredit：').grid(row=3)
    Label(course_frame, text='Croom：').grid(row=4)
    entry1 = Entry(course_frame)
    entry1.grid(row=1, column=2)
    cno = StringVar()
    entry1["textvariable"] = cno
    entry2 = Entry(course_frame)
    entry2.grid(row=2, column=2)
    cname = StringVar()
    entry2["textvariable"] = cname
    entry3 = Entry(course_frame)
    entry3.grid(row=3, column=2)
    ccredit = StringVar()
    entry3["textvariable"] = ccredit
    entry4 = Entry(course_frame)
    entry4.grid(row=4, column=2)
    croom = StringVar()
    entry4["textvariable"] = croom
    Button(course_frame, text='delete', command=delete_course).grid(row=5, column=0)
    Button(course_frame, text='insert', command=insert_course).grid(row=5, column=1)
    Button(course_frame, text='search', command=search_course).grid(row=5, column=2)
    course_frame.grid(row=1, column=0)

    proj_frame = Frame(root_frame)
    Label(proj_frame, text='Project', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(proj_frame, text='Pname：').grid(row=1)
    Label(proj_frame, text='PLno：').grid(row=2)
    entry1 = Entry(proj_frame)
    entry1.grid(row=1, column=2)
    pname = StringVar()
    entry1["textvariable"] = pname
    entry2 = Entry(proj_frame)
    entry2.grid(row=2, column=2)
    plno = StringVar()
    entry2["textvariable"] = plno
    Button(proj_frame, text='delete', command=delete_project).grid(row=3, column=0)
    Button(proj_frame, text='insert', command=insert_project).grid(row=3, column=1)
    Button(proj_frame, text='search', command=search_project).grid(row=3, column=2)
    proj_frame.grid(row=1, column=1)

    room_frame = Frame(root_frame)
    Label(room_frame, text='Classroom', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(room_frame, text='Rno：').grid(row=1)
    Label(room_frame, text='Rbuilding：').grid(row=2)
    Label(room_frame, text='Rcapacity：').grid(row=3)
    entry1 = Entry(room_frame)
    entry1.grid(row=1, column=2)
    rno = StringVar()
    entry1["textvariable"] = rno
    entry2 = Entry(room_frame)
    entry2.grid(row=2, column=2)
    rbuilding = StringVar()
    entry2["textvariable"] = rbuilding
    entry3 = Entry(room_frame)
    entry3.grid(row=3, column=2)
    rcapacity = StringVar()
    entry3["textvariable"] = rcapacity
    Button(room_frame, text='delete', command=delete_classroom).grid(row=4, column=0)
    Button(room_frame, text='insert', command=insert_classroom).grid(row=4, column=1)
    Button(room_frame, text='search', command=search_classroom).grid(row=4, column=2)
    room_frame.grid(row=1, column=2)

    sc_frame = Frame(root_frame)
    Label(sc_frame, text='SC', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(sc_frame, text='Sno：').grid(row=1)
    Label(sc_frame, text='Cno：').grid(row=2)
    Label(sc_frame, text='Grade：').grid(row=3)
    entry1 = Entry(sc_frame)
    entry1.grid(row=1, column=2)
    sc_sno = StringVar()
    entry1["textvariable"] = sc_sno
    entry2 = Entry(sc_frame)
    entry2.grid(row=2, column=2)
    sc_cno = StringVar()
    entry2["textvariable"] = sc_cno
    entry3 = Entry(sc_frame)
    entry3.grid(row=3, column=2)
    grade = StringVar()
    entry3["textvariable"] = grade
    Button(sc_frame, text='delete', command=delete_sc).grid(row=4, column=0)
    Button(sc_frame, text='insert', command=insert_sc).grid(row=4, column=1)
    Button(sc_frame, text='search', command=search_sc).grid(row=4, column=2)
    sc_frame.grid(row=2, column=0)

    tc_frame = Frame(root_frame)
    Label(tc_frame, text='TC', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(tc_frame, text='Tno：').grid(row=1)
    Label(tc_frame, text='Cno：').grid(row=2)
    Label(tc_frame, text='Hours：').grid(row=3)
    entry1 = Entry(tc_frame)
    entry1.grid(row=1, column=2)
    tc_tno = StringVar()
    entry1["textvariable"] = tc_tno
    entry2 = Entry(tc_frame)
    entry2.grid(row=2, column=2)
    tc_cno = StringVar()
    entry2["textvariable"] = tc_cno
    entry3 = Entry(tc_frame)
    entry3.grid(row=3, column=2)
    hours = StringVar()
    entry3["textvariable"] = hours
    Button(tc_frame, text='delete', command=delete_tc).grid(row=4, column=0)
    Button(tc_frame, text='insert', command=insert_tc).grid(row=4, column=1)
    Button(tc_frame, text='search', command=search_tc).grid(row=4, column=2)
    tc_frame.grid(row=2, column=1)

    pp_frame = Frame(root_frame)
    Label(pp_frame, text='PP', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(pp_frame, text='Tno：').grid(row=1)
    Label(pp_frame, text='Pname：').grid(row=2)
    entry1 = Entry(pp_frame)
    entry1.grid(row=1, column=2)
    pp_tno = StringVar()
    entry1["textvariable"] = pp_tno
    entry2 = Entry(pp_frame)
    entry2.grid(row=2, column=2)
    pp_pname = StringVar()
    entry2["textvariable"] = pp_pname
    Button(pp_frame, text='delete', command=delete_pp).grid(row=3, column=0)
    Button(pp_frame, text='insert', command=insert_pp).grid(row=3, column=1)
    Button(pp_frame, text='search', command=search_pp).grid(row=3, column=2)
    pp_frame.grid(row=2, column=2)

    pt_frame = Frame(root_frame)
    Label(pt_frame, text='Project_Teacher', font=('Times New Roman', 10, 'bold')).grid(row=0)
    Label(pt_frame, text='Pname：').grid(row=1)
    Label(pt_frame, text='Tname：').grid(row=2)
    entry1 = Entry(pt_frame)
    entry1.grid(row=1, column=2)
    pt_pname = StringVar()
    entry1["textvariable"] = pt_pname
    entry2 = Entry(pt_frame)
    entry2.grid(row=2, column=2)
    pt_tname = StringVar()
    entry2["textvariable"] = pt_tname
    Button(pt_frame, text='leader', command=pt_leader).grid(row=3, column=1)
    Button(pt_frame, text='participant', command=pt_participant).grid(row=3, column=2)
    pt_frame.grid(row=3, column=1)

    root.mainloop()
