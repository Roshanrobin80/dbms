import mysql.connector

con=mysql.connector.connect(user='roshanrobin',host='localhost',password='xamppass#01',database='batch7')
cur=con.cursor()
con.autocommit=True
# cur.execute("create database batch7")
# try:
#     cur.execute("create table std (roll int,name text,age int)")
# except:
#     pass

# roll=int(input('enter your roll number : '))
# name=input('enter your name : ')
# age=int(input('enter your age : '))

# cur.execute("insert into std (roll,name,age)values(%s,%s,%s)",(roll,name,age))

# cur.execute("select * from std order by name desc")
# cur.execute("select * from std where name like 'a%'")
# cur.execute("select * from std where name like 'a")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("create table mark (roll int,sub text,mark int)")

# cur.execute("insert into mark(roll,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
cur.execute("select std.roll,std.name,std.age,mark.sub,mark.mark from std cross join mark")
data=cur.fetchall()
for i in data:
    print(i)
# data=con.execute("select name,count(age) from std group by name")
# for i in data:
#     print(i)


      
