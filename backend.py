import pymysql as py
import pandas as pd
import matplotlib as mplot

con = py.connect('127.0.0.1', 'root', '', 'ICT')
cur = con.cursor()


def facultyLogin(usr, pwd):
    qry = "select * from faculty where Emailid = '%s'" % (usr)
    cur.execute(qry)
    row = cur.fetchone()
    con.commit()
    if row is None:
        return False
    else:
        if pwd in row:
            return True
        else:
            return False


def studnetLogin(usr, pwd):
    qry = "select password from users where Emailid = '%s'" % (usr)
    cur.execute(qry)
    row = cur.fetchone()
    con.commit()
    if row is None:
        return False
    else:
        if pwd in row:
            return True
        else:
            return False


def registerStudent():
    name = input('Enter your Name : ')
    roll = input('Enter your Roll No : ')
    email = input('Enter your Email Id : ')
    pwd = input('Enter your Password : ')
    course = input('Enter course Name : ')
    try:
        qry = "insert into users(Name, Rollno, Emailid, password, Course) values('%s', '%s', '%s', '%s', '%s')" % (
            name, roll, email, pwd, course)
        cur.execute(qry)
        con.commit()
        print ("Student Registered Successfully....")
    except Exception:
        print ("Record with same Roll No or Email already Exist...")


def showStudent():
    qry = "select * from users"
    df = pd.read_sql(qry, con)
    # print(df[['Name', 'Rollno', 'Emailid', 'Course', 'DateOfReg']])
    print(df)


def addDataRecord(filename, usr):
    qry = "select * from users"
    df1 = pd.read_sql(qry, con)
    data = df1[df1.Emailid == usr]
    x = df1.index[df1.Emailid == usr].tolist()
    i = x[0]
    try:
        qry1 = "insert into filerecord( Name, Rollno, Emailid, Course, filename, Status) values('%s', '%s', '%s', '%s', '%s', '%s')" % (
            data.Name[i], data.Rollno[i], usr, data.Course[i], filename, "Submitted")
        cur.execute(qry1)
        con.commit()
    except Exception:
        print ("Assignment already uploaded...")


def showFileRecord():
    qry = "select * from filerecord"
    df = pd.read_sql(qry, con)
    if df.empty:
        print ("Record is Empty...")

    else:
        print (df)


def showCheatRecord():
    qry = "select * from cheatrecord"
    df = pd.read_sql(qry, con)
    if df.empty:
        print ("Record is Empty...")

    else:
        print (df)


def updateQuery(qry):
    cur.execute(qry)
    con.commit()


def showParticularRecord(usr):
    qry = 'select * from filerecord where Emailid = "%s"' % (usr)
    df = pd.read_sql(qry, con)
    if df.empty:
        qry = 'select * from cheatrecord where Emailid = "%s"' % (usr)
        df = pd.read_sql(qry, con)
        if df.empty:
            print ("Your assignment is not uploaded yet...")
        else:
            print (df)
    else:
        print (df)


def cheatRecord(filename1, filename2, usr):
    qry = "select * from users"
    df1 = pd.read_sql(qry, con)
    data = df1[df1.Emailid == usr]
    x = df1.index[df1.Emailid == usr].tolist()
    i = x[0]
    try:
        qry1 = "insert into cheatrecord( Name, Rollno, Emailid, Course, filename, Status) values('%s', '%s', '%s', '%s', '%s', '%s')" % (
            data.Name[i], data.Rollno[i], usr, data.Course[i], filename1, "Cheated")
        cur.execute(qry1)
        con.commit()
        temp = "update filerecord set Status = 'Cheated' where filename = '%s'" % (filename2)
        updateQuery(temp)
    except Exception:
        print ("You have already tried to copied your Assignment....")
