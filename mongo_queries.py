from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
db = client.practicum12024

# Ensure indexes are created
db.strikes.create_index('fid')
db.flights.create_index('fid')
db.flights.create_index('originAirport')
db.airports.create_index('aid')
db.flights.create_index('ailid')
db.airlines.create_index('ailid')
db.strikes.create_index('wid')
db.wildlife.create_index('wid')
db.conditions.create_index('cid')

# Function to execute and print the query result
def execute_query(query):
    for doc in query:
        pprint(doc)

# 1. Total Number of Strikes
total_strikes = db.strikes.count_documents({})
print(f'Total Strikes: {total_strikes}')

# 2. Strikes by Airport
strikes_by_airport = db.strikes.aggregate([
    {
        '$lookup': {
            'from': 'flights',
            'localField': 'fid',
            'foreignField': 'fid',
            'as': 'flight_info'
        }
    },
    {'$unwind': '$flight_info'},
    {
        '$lookup': {
            'from': 'airports',
            'localField': 'flight_info.originAirport',
            'foreignField': 'aid',
            'as': 'airport_info'
        }
    },
    {'$unwind': '$airport_info'},
    {
        '$group': {
            '_id': '$airport_info.airportName',
            'num_strikes': {'$sum': 1}
        }
    },
    {'$sort': {'num_strikes': -1}},
    {'$limit': 10}
])
print("Strikes by Airport:")
execute_query(strikes_by_airport)

# 3. Strikes by Airline
strikes_by_airline = db.strikes.aggregate([
    {
        '$lookup': {
            'from': 'flights',
            'localField': 'fid',
            'foreignField': 'fid',
            'as': 'flight_info'
        }
    },
    {'$unwind': '$flight_info'},
    {
        '$lookup': {
            'from': 'airlines',
            'localField': 'flight_info.ailid',
            'foreignField': 'ailid',
            'as': 'airline_info'
        }
    },
    {'$unwind': '$airline_info'},
    {
        '$group': {
            '_id': '$airline_info.name',
            'num_strikes': {'$sum': 1}
        }
    },
    {'$sort': {'num_strikes': -1}},
    {'$limit': 10}
])
print("Strikes by Airline:")
execute_query(strikes_by_airline)

# 4. Strikes by Wildlife Size
strikes_by_size = db.strikes.aggregate([
    {
        '$lookup': {
            'from': 'wildlife',
            'localField': 'wid',
            'foreignField': 'wid',
            'as': 'wildlife_info'
        }
    },
    {'$unwind': '$wildlife_info'},
    {
        '$group': {
            '_id': '$wildlife_info.size',
            'num_strikes': {'$sum': 1}
        }
    },
    {'$sort': {'num_strikes': -1}},
    {'$limit': 10}
])
print("Strikes by Wildlife Size:")
execute_query(strikes_by_size)
