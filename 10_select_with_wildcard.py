import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()


cursor.execute("SELECT * FROM movies where name like '%vikins%' ")

result = cursor.fetchone()

print(result)