# AUTHOR:- KUSH SHAH
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky117@",
  database="mydatabase2"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")