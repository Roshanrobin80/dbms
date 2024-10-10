#create

import sqlite3
con = sqlite3.connect("dbms/batch7.db")
try:
    con.execute("create table std(roll_no int,name text,age int)")

except:
    pass

import sqlite3
con = sqlite3.connect("dbms/batch7.db")
try:
    con.execute("create table mark(roll_no int,sub text,mark int)")

except:
    pass
# con.execute("insert into std(roll_no,name,age)values(1,'liya',18),(2,'aparna',20),(3,'nora',18)")
# con.commit()
con.execute("insert into mark(roll_no,sub,mark)values(1,'cs',75),(1,'che',70),(2,'cs',65),(4,'py',55)") 
con.commit()
# roll=int(input("Enter roll no :"))
# name=input("Enter name :")
# age=int(input("Enter age :"))
# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()
# data=con.execute("select * from std where name = 'nora'")
# for i in data:
#     print(i)

#update

'''roll_no=int(input('Enter a roll no :'))
data=con.execute("select * from std where roll_no=?",(roll_no,))
for i in data:
    print(i)'''


'''name=str(input('Enter old name :'))
name1=str(input('Enter new name :'))
con.execute("update std set name=? where name=?",(name1,name))
con.commit()'''

#delete

'''roll_no=int(input('Enter a roll no :'))
con.execute("delete from std where roll_no=?",(roll_no,))
con.commit()'''

#search by alphabet

'''data=con.execute("select * from std where name like '_a%rrr' ")
for i in data:
    print(i)'''

#order(ascending & descending)

'''data=con.execute("select * from std order by name")
for i in data:
    print(i)'''

'''data=con.execute("select * from std order by name desc")
for i in data:
    print(i)'''
