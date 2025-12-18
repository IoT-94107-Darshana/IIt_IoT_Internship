import mysql.connector
from datetime import datetime
Connection=mysql.connector.connect (
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smartAgri",
    use_pure = True
)

query = "select * from soil_moisture";


cursor = Connection.cursor()

cursor.execute(query)

soil_moisture= cursor.fetchall()


for soil_moisture in soil_moisture:
    print(soil_moisture)
    
cursor.close()

Connection.close()