import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="duelingcarls",
  database = "menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, birth, MONTH(birth) FROM pet")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
