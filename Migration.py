import mysql.connector
from pymongo import MongoClient
from datetime import datetime, date

# MySQL connection
mysql_conn = mysql.connector.connect(
    host="db4free.net",
    user="dhivya",
    password="Practicum@2024",
    database="practicum12024"
)

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['practicum12024']

# Function to convert dates to datetime objects
def convert_dates(record):
    for key, value in record.items():
        if isinstance(value, date):
            record[key] = datetime.combine(value, datetime.min.time())
    return record

# Function to migrate data from MySQL to MongoDB
def migrate_table(table_name):
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if rows:
        rows = [convert_dates(row) for row in rows]  # Convert dates to datetime
        mongo_db[table_name].insert_many(rows)
    cursor.close()

# List of tables to migrate
tables = ['airports', 'aircrafts', 'airlines', 'wildlife', 'flights', 'conditions', 'strikes']

# Migrate each table
for table in tables:
    migrate_table(table)

# Close connections
mysql_conn.close()
mongo_client.close()
