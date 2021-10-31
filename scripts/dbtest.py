#!C:\Users\Sigma\AppData\Local\Programs\Python\Python39\python.exe
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="r6eAbana@wasak1",
  database="sas"
)
sku = "gdkgdsgjsb"

preparedinsert = "INSERT INTO "+sku+"('review') VALUES(%s)"
print(preparedinsert)
#mycursor = mydb.cursor()

#mycursor.execute(""+prestmt)