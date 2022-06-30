import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()


# sql = "UPDATE movies SET polt = 'update2' WHERE name='breaking bad'"
sql = "UPDATE movies SET language =%s"
val = ('ar',)
cursor.execute(sql,val)

conn.commit()

print('done')