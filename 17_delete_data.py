import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()


sql = "DELETE FROM movies WHERE name =%s"
val = ('vikins',)
cursor.execute(sql,val)

conn.commit()

print('done')