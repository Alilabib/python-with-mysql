import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()

# sql = "Alter TABLE movies ADD COLUMN language VARCHAR(30)"

sql = "Alter TABLE movies CHANGE COLUMN language language VARCHAR(50)"

cursor.execute(sql)

conn.commit()

print('done')