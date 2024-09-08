
# API Integration Project - Streamlining Data Access

## Project Overview
This project focuses on streamlining data access by integrating multiple APIs and databases, including MongoDB and MySQL. The integration process is automated using Python scripts, which handle data retrieval, insertion, and querying efficiently.

## Project Structure
Here’s a brief explanation of the key files in this repository:

- **`app.py`**: The main application file that coordinates the API integration and data processing logic.
- **`mongo_queries.py`**: Contains MongoDB queries, including index creation for efficient data access and management.
- **`Migration.py`**: Handles the migration of data between different databases, ensuring data consistency and integrity.
- **`Insertion.md`**: Documentation outlining the procedures for inserting data into the databases.
- **`BirdStrikesData-V3.csv`**: A sample dataset used within the project to demonstrate the data integration and querying process.
- **`templates/`**: Contains any template files used for data formatting or report generation.

## Prerequisites
Before running the project, ensure you have the following installed:

- **Python 3.x**
- **MongoDB**
- **MySQL**
- **Flask**
- **pymongo**
- **Other dependencies listed in `requirements.txt`**

## Installation
Follow these steps to set up and run the project:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/DhivyaKumar02/API-Integration-Project-Streamlining-Data-Access.git
   cd API-Integration-Project-Streamlining-Data-Access
   ```

2. **Install Dependencies:**

   Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Database Connections:**

   Update the database connection strings in `app.py` and `mongo_queries.py` to match your local MongoDB and MySQL setup.

4. **Run the Application:**

   Execute the main application script:

   ```sh
   python app.py
   ```

## Features
- **API Integration**: Combines data from multiple APIs into a unified database.
- **Automated Data Management**: Automates data insertion and querying across MongoDB and MySQL databases.
- **Indexing**: Ensures efficient data access through index creation in MongoDB.

## Usage
- **Data Insertion**: Detailed in `Insertion.md`, this process outlines how data from the CSV file is inserted into the databases.
- **Data Queries**: Use the functions in `mongo_queries.py` to interact with and retrieve data from MongoDB.

