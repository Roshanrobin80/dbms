import mysql.connector

con=mysql.connector.connect(user='roshanrobin',host='localhost',password='xamppass#01',database='batch7')
cur=con.cursor()
con.autocommit=True
# cur.execute("create database batch7")

cur.execute("create table std (roll int,name text,age int)")
roll=int(input("Enter roll no :"))
name=input("Enter a name :")
age=int(input("Enter age :"))
cur.execute("insert into std(roll,name,age)values(%s,%s,%s)"),(roll,name,age)
      
