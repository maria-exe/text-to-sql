# MySQL
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

cursor.close()  
db1.close()


# Postgresql
import psycopg2

db2 = psycopg2.connect (
host="localhost",
database="movies",
user="postgres",
password="123456"
)

cursor = db2.cursor() 
cursor.execute("Select * from actor_role")
data = cursor.fetchall()

for linha in data:
    print(linha)

