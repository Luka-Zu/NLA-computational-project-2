from pprint import pprint

import requests


# "https://api.openweathermap.org/data/2.5/forecast?lat=40.7&lon=-73.9&appid=04643437329dc66bd813e2ac3cf135e0&units=metric"


class Weather:
    """
    Using restful API I get information about current humidity and temperature in cities
    API_KEY : "04643437329dc66bd813e2ac3cf135e0"
    """
    base_URL = "https://api.openweathermap.org/data/2.5/forecast?"

    def __init__(self, city, apikey="04643437329dc66bd813e2ac3cf135e0"):
        req = requests.get(f"{self.base_URL}q={city}&appid={apikey}&units=metric")
        self.data = req.json()

    def get_data(self):
        relevant_data = self.data['list'][0]['main']

        return {
            "temp": relevant_data["temp"],
            "humidity": relevant_data["humidity"],
        }

    def get_raw_data(self):
        relevant_data = self.data['list'][0]['main']

        return [
            relevant_data["temp"],
            relevant_data["humidity"],
        ]



