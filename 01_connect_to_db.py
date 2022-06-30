import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    port=8889,
    user="root",
    passwd="root"
)

mycursor = myconn.cursor()

print("Connectd")

mycursor.execute("SHOW DATABASES")