import mysql.connector
from datetime import datetime
connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data31",
    use_pure=True

)
query=f"select * from sensors where temperature<50;"
cursor=connection.cursor()
cursor.execute(query)
sensors = cursor.fetchall()
for s in sensors :
    print(s)
cursor.close()
connection.close()