import requests
import os
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/36a8b23504f2db994cf6c3c9ec104cde/flightDeals/prices"
SHEETY_HEADERS = {
            "Authorization": f"Bearer {os.environ.get('TOKEN')}"
        }


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(put_endpoint, json=new_data, headers=SHEETY_HEADERS)
            print(response.text)
