import mysql.connector

conn = mysql.connector.connect(
    host ="localhost",
    port =8889,
    user ="root",
    passwd="root",
    database="pydatabase"
)

cursor = conn.cursor()

#sql = "DROP TABlE movies "

sql = "DROP TABlE IF EXISTS movies"

cursor.execute(sql)

conn.commit()

print('done')