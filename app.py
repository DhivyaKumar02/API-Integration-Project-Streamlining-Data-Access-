from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app)

# MySQL Database Connection Configuration
db_user = 'dhivya'
db_password = 'Practicum@2024'
db_name = 'practicum12024'
db_host = 'db4free.net'
db_port = 3306

def get_db_connection():
    conn = pymysql.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host=db_host,
        port=db_port
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

def run_query(query):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result
    finally:
        conn.close()

class Analyses(Resource):
    def get(self):
        analyses = {}

        queries = {
            "total_strikes_by_airline": "SELECT airlineName, COUNT(*) AS total_strikes FROM flights JOIN strikes ON flights.fid = strikes.fid GROUP BY airlineName ORDER BY total_strikes DESC",
            "strikes_by_month": "SELECT DATE_FORMAT(date, '%Y-%m') AS month, COUNT(*) AS total_strikes FROM flights JOIN strikes ON flights.fid = strikes.fid GROUP BY month ORDER BY month",
            "strikes_by_airport": "SELECT airportName, COUNT(*) AS total_strikes FROM airports JOIN flights ON airports.aid = flights.originAirport JOIN strikes ON flights.fid = strikes.fid GROUP BY airportName ORDER BY total_strikes DESC",
            "strikes_by_sky_condition": "SELECT sky_condition, COUNT(*) AS total_strikes FROM conditions JOIN strikes ON conditions.cid = strikes.conditions GROUP BY sky_condition ORDER BY total_strikes DESC",
            "damage_by_altitude": "SELECT altitude, SUM(damage) AS total_damage, COUNT(*) AS total_strikes FROM strikes GROUP BY altitude ORDER BY altitude",
            "strikes_by_heavy_aircraft": "SELECT isHeavy, COUNT(*) AS total_strikes FROM flights JOIN strikes ON flights.fid = strikes.fid GROUP BY isHeavy",
            "impact_by_bird_strike": "SELECT impact, COUNT(*) AS total_strikes FROM strikes GROUP BY impact"
        }

        for key, query in queries.items():
            analyses[key] = run_query(query)

        return jsonify(analyses)

api.add_resource(Analyses, '/analyses')

if __name__ == '__main__':
    app.run(debug=True)
