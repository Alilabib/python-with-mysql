import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    port=8889,
    user="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()


cursor.execute(" CREATE TABLE movies(name VARCHAR(100), polt VARCHAR(20))")
print("Table Create Successfully")