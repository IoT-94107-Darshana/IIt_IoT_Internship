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
id =  int(input("enter id :"))
temperature = float(input("enter temperture : "))
humidity = float(input("enter humidity :"))
timestamp = datetime.fromisoformat(input("eneter date and time : "))

query = f"insert into sensors values({id}, {temperature}, {humidity}, '{timestamp}');"
cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()
cursor.close()
Connection.close()