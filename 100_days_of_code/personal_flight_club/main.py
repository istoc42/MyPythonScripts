#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager

SHEET_ENDPOINT = "https://api.sheety.co/14a50286cbf0a4097606b4436b42adad/flightDeals/prices"

sheet_data = [
    {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, 
    {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, 
    {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, 
    {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, 
    {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, 
    {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, 
    {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, 
    {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, 
    {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}
    ]

fs = FlightSearch()
dm = DataManager()

for city in sheet_data:
    if city['iataCode'] == '':
        iata = fs.get_iataCode(city['city'])
        city_id = city['id']
        city['iataCode'] = iata
        dm.update_row(city_id, iata)

