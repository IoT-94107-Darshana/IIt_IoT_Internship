import mysql.connector
from datetime import datetime
connection=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smartAgri",
    use_pure=True

)
query=f"select * from soil_moisture where moisture<50;"
cursor=connection.cursor()
cursor.execute(query)
soil_moisture = cursor.fetchall()
for s in soil_moisture :
    print(s)
cursor.close()
connection.close()