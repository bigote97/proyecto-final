from credentials import getCredentials
import mysql.connector


mydb = mysql.connector.connect(**getCredentials())

mycursor = mydb.cursor()
query = "SELECT * FROM provincias"
mycursor.execute(query)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)