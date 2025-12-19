from utils.dbconnection import getBDConnection
def executeQuery(query):
    connection = getBDConnection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
