import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()
sql = "SELECT * FROM movies ORDER BY name DESC"

cursor.execute(sql)

result = cursor.fetchall()

print(result)