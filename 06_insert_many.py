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
data =[
    ("Person Break","escap plan"),
    ("vikins" ,"old heros")
]
cursor.executemany(sql , data)
conn.commit()
print("data inserted")
print(cursor.rowcount)