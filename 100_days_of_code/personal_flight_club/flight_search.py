import requests

API_KEY = "3r8UrxytDPSVPiNa1n_dQ3bkIQ8pQR9N"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iataCode(self, city_name):
        self.city = city_name

        param = {
            "terms": self.city,
        }

        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url=TEQUILA_ENDPOINT, params=param, headers=headers)
        
        self.iata = response['locations']['id']