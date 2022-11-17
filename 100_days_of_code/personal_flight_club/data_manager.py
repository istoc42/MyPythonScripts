import requests
import json

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def update_row(self, city_id, iataCode):
        self.city_id = city_id
        self.iataCode = iataCode

        PUT_URL = f"https://api.sheety.co/14a50286cbf0a4097606b4436b42adad/flightDeals/prices/{self.city_id}"

        params = {
            "price": {
                "iataCode": f"{self.iataCode}",
                "id": f"{self.city_id}",
            }
        }
  
        params_json = json.dumps(params)

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(url=PUT_URL, verify=False, data=params_json, headers=headers)
        print(response.text)