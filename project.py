
## My SQL
import MySQLdb

db1 = MySQLdb.connect(
    "localhost",
    "root",
    "983148",
    "movie"
)

cursor = db1.cursor()
cursor.execute("Select * from actors")
empl_data = cursor.fetchall()

for linha in empl_data:
    print(linha)


db1.close()
cursor.close()

# PostgreSQP
import psycopg2

db2 = psycopg2.connect (
    host='localhost',
    user='user',
    password='983148',
    db='employees'
)