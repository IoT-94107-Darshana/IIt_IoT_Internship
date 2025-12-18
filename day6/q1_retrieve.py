import mysql.connector
from datetime import datetime
Connection=mysql.connector.connect (
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data31",
    use_pure = True
)

query = "select * from sensors";

cursor = Connection.cursor()

cursor.execute(query)

sensors = cursor.fetchall()

for sensors in sensors:
    print(sensors)
    
cursor.close()

Connection.close()