import requests
import pandas as pd
from datetime import datetime
from pymongo import MongoClient

# MongoDB URI (replace with your actual credentials)
MONGO_URI = "mongodb+srv://rs7267887611:r18a1j10@air-pollutant-data.uf29efr.mongodb.net/?retryWrites=true&w=majority&appName=air-pollutant-datay"

# MongoDB connection with SSL/TLS settings (disable SSL validation for testing)
try:
    # Disabling SSL certificate verification (use with caution, only for testing)
    client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
    print("MongoDB connected successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

# Connect to MongoDB database
db = client['air_quality_data']

# Generate collection name as current date and timestamp (DD/MM/YYYY-HH:MM:SS)
current_timestamp = datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
collection_name = current_timestamp

# Dynamically create collection using the generated name
collection = db[collection_name]

# Replace with your actual token
TOKEN = '536eb79029c66d0592e5252536b5dfe4298c4e65'

# Load the CSV file containing the station data
file_path = 'Air_Pollution_Stations.csv'  # Your uploaded file path
pollution_stations_df = pd.read_csv(file_path)

# Prepare a list to store all the fetched complete data
all_station_data = []

# Loop through each row in the CSV and fetch data for each station
for index, row in pollution_stations_df.iterrows():
    state = row['State/UT']
    city = row['City']
    station_name = row['Station Name']
    idx = row.get('idx', None)  # Assuming idx is provided in the CSV file
    
    # First attempt to fetch data using city name
    url_city = f'https://api.waqi.info/feed/{city}/?token={TOKEN}'
    response_city = requests.get(url_city)
    data = response_city.json()

    # If data fetch using city name fails, try fetching using idx
    if data['status'] != 'ok' and idx:
        url_idx = f'https://api.waqi.info/feed/{idx}/?token={TOKEN}'
        response_idx = requests.get(url_idx)
        data = response_idx.json()
    
    # Check if the request was successful
    if data['status'] == 'ok':
        # Prepare the data for saving, including the complete API response
        station_data = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'state': state,
            'city': city,
            'station_name': station_name,
            'idx': idx,
            'complete_api_response': data  # Save the complete response
        }
        
        # Append the data to the list
        all_station_data.append(station_data)

        # Insert data into MongoDB collection
        try:
            collection.insert_one(station_data)  # Insert the document into MongoDB
            print(f"Data fetched and stored for station: {station_name}")
        except Exception as e:
            print(f"Failed to insert data for station {station_name}: {e}")
    else:
        print(f"Failed to retrieve data for station: {station_name}")

# Optionally, save all the fetched data (including complete API responses) to a JSON file
# with open('all_station_complete_air_quality_data.json', 'w') as json_file:
#     json.dump(all_station_data, json_file, indent=4)

print("All complete data has been successfully fetched and saved in database")
