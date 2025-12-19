from flask import Flask, request, jsonify
from utils.executequery import executeQuery
from utils.executeselectquery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture', methods=['POST'])
def create_data():
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')


    query = (
        f"INSERT INTO sensors (id, temperture, humidity) "
        f"VALUES ({id}, {temperature}, '{humidity}');"
    )
    executeQuery(query=query)
    return "Soil moisture data added successfully"

@server.route('/sensors', methods=['GET'])
def retrieve_sensors():
    query = "SELECT * FROM sensors;"
    data = executeSelectQuery(query=query)
    return jsonify(data)

@server.route('/sensors', methods=['PUT'])
def update_sensors():
    id = request.form.get('id')
    temperature = request.form.get('temperture')

    query = (
        f"UPDATE sensors "
        f"SET temperture = {temperature} "
        f"WHERE id = {id};"
    )
    executeQuery(query=query)
    return "temperature updated successfully"

@server.route('/sensors', methods=['DELETE'])
def delete_sensors():
    id = request.form.get('id')

    query = f"DELETE FROM sensors WHERE id = {id};"
    executeQuery(query=query)
    return "sensors record deleted successfully"

@server.route('/sensors/filter', methods=['GET'])
def filter_sensors():
    temperature = request.args.get('temperature')

    query = f"SELECT * FROM sensors WHERE temperature < {temperature};"
    data = executeSelectQuery(query=query)
    return jsonify(data)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
