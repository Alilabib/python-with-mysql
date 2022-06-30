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
sql = "UPDATE movies SET polt = 'update2'"

cursor.execute(sql)

conn.commit()

print('done')