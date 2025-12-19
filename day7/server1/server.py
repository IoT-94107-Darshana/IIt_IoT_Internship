from flask import Flask, request, jsonify
from utils.executequery import executeQuery
from utils.executeselectquery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/soil_moisture', methods=['POST'])
def create_data():
    sensor_id = request.form.get('sensor_id')
    moisture = request.form.get('moisture')
    reading_time = request.form.get('reading_time')

    query = (
        f"INSERT INTO soil_moisture (sensor_id, moisture, reading_time) "
        f"VALUES ({sensor_id}, {moisture}, '{reading_time}');"
    )
    executeQuery(query=query)
    return "Soil moisture data added successfully"

@server.route('/soil_moisture', methods=['GET'])
def retrieve_soil_moisture():
    query = "SELECT * FROM soil_moisture;"
    data = executeSelectQuery(query=query)
    return jsonify(data)

@server.route('/soil_moisture', methods=['PUT'])
def update_soil_moisture():
    sensor_id = request.form.get('sensor_id')
    moisture = request.form.get('moisture')

    query = (
        f"UPDATE soil_moisture "
        f"SET moisture = {moisture} "
        f"WHERE sensor_id = {sensor_id};"
    )
    executeQuery(query=query)
    return "Moisture updated successfully"

@server.route('/soil_moisture', methods=['DELETE'])
def delete_soil_moisture():
    sensor_id = request.form.get('sensor_id')

    query = f"DELETE FROM soil_moisture WHERE sensor_id = {sensor_id};"
    executeQuery(query=query)
    return "Soil moisture record deleted successfully"

@server.route('/soil_moisture/filter', methods=['GET'])
def filter_soil_moisture():
    moisture = request.args.get('moisture')

    query = f"SELECT * FROM soil_moisture WHERE moisture < {moisture};"
    data = executeSelectQuery(query=query)
    return jsonify(data)

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
