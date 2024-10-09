import sqlite3
con = sqlite3.connect("dbms/batch7.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass
# con.execute("insert into std(roll_no,name,age)values(1,'liya',18),(2,'aparna',20),(3,'nora',18)")
# con.commit()
roll=int(input("Enter roll no :"))
name=input("Enter name :")
age=int(input("Enter age :"))
con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()