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
sensor_id =  int(input("enter sensor_id :"))
moisture = float(input("enter moisture: "))
reading_time=datetime.fromisoformat(input("enetr date and time :"))

query = f"insert into soil_moisture values({sensor_id}, {moisture},  '{reading_time}');"

cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()
cursor.close()
Connection.close()