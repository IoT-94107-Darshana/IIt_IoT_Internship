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
# form a query to be executed
id = int(input("Enter id  of a sensors to be deleted : "))

query = f"delete from sensors where id  = {id};"

# create a cursor to execute a query
cursor = Connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
Connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
Connection.close()

