import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()
#sql = "SELECT * FROM movies LIMIT 3"
sql = "SELECT * FROM movies LIMIT 3 OFFSET 2"

cursor.execute(sql)

result = cursor.fetchall()

print(result)