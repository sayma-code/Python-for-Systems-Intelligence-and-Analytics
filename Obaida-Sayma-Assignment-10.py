#!/usr/bin/python3
#importing mysql connector
import mysql.connector

#connecting to mysql database
mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

#printing the connection
print(mydb1) 
#creating a cursor object to execute SQL commands
mycursor1 = mydb1.cursor()
#mycursor1.execute("DROP DATABASE mydatabase")
#creating a database named mydatabase
mycursor1.execute("CREATE DATABASE mydatabase")
#listing all databases
mycursor1.execute("SHOW DATABASES")
for x in mycursor1:
  print(x) 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)
#5. Creating a table named customers
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#showing all tables in the database
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x) 


#6. Creating first record
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Wolffintie 32, FIN-65101 Vaasa, Finland")
mycursor.execute(sql, val)
mydb.commit()
#7. Creating second record
val = ("Jane", "Wolffintie 32, FIN-65101 Vaasa, Finland")
mycursor.execute(sql, val)
mydb.commit()
#8. Printing all records in the customers table MySQL Select
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#9. MySQL Where
sql = "SELECT * FROM customers WHERE address ='Wolffintie 32, FIN-65101 Vaasa, Finland'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
   print(x)
#10. MySQL Order By
mycursor.execute("SELECT * FROM customers ORDER BY name")
myresult = mycursor.fetchall()
for x in myresult:
   print(x)

#11. Creating third record
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Jim Doe", "Wolffintie 32, FIN-65101 Vaasa, Finland")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#12. Print where name is Jim Doe
sql = "SELECT * FROM customers WHERE name ='Jim Doe'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
   print(x)

#13. Deleting the record where name is Jim Doe
sql = "DELETE FROM customers WHERE name ='Jim Doe'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record deleted")
#mycursor1.execute("DROP DATABASE mydatabase2")
#14. Create a database named mydatabase2
mycursor1.execute("CREATE DATABASE mydatabase2")
mycursor1.execute("SHOW DATABASES")
for x in mycursor1:
  print(x)

#15. Create a table named customers2 in mydatabase2
mydb3 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)
#Creating a table named customers2
mycursor3 = mydb3.cursor()
mycursor3.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#showing all tables in the database
mycursor3.execute("SHOW TABLES")
for x in mycursor3:
  print(x)

#16. Deleting the table customers2 in mydatabase2
mycursor3.execute("DROP TABLE customers2")
mycursor3.execute("SHOW TABLES")
for x in mycursor3:
  print(x)

#17. Deleting the database mydatabase2
mycursor1.execute("DROP DATABASE mydatabase2")
mycursor1.execute("SHOW DATABASES")
for x in mycursor1:
  print(x)

