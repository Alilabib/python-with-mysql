import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    port=8889,
    user="root",
    passwd="root"
)

mycursor = myconn.cursor()

mycursor.execute("CREATE DATABASE pydatabase")