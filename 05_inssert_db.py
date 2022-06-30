import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()

sql = "INSERT INTO movies(name , polt) VALUES (%s , %s)"
data = ("Fast 5","Magic")

cursor.execute(sql , data)

conn.commit()
print("data inserted")
print(cursor.rowcount)