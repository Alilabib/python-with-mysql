import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()
sql = "SELECT * FROM movies where name=%s"
data = ('vikins',)
cursor.execute(sql , data)

result = cursor.fetchone()

print(result)