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

id = int(input("Enter id  whose humidity to be updated : "))
humidity= float(input("Enter new humidity : "))

query = f"update sensors SET humidity = {humidity} where id = {id};"

cursor = Connection.cursor()
cursor.execute(query)
Connection.commit()
cursor.close()
Connection.close()
