import requests

class OpenAQClient:
    BASE_URL = "https://api.openaq.org/v3"

    def __init__(self, api_key: str):
        self.headers = {"x-api-key": api_key}

    def get_brazil_locations(self, limit: int = 100, page: int = 1):
        url = f"{self.BASE_URL}/locations"
        params = {
            "countries_id": 45,    
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()["results"]

    def get_sensor_location(self, location_id: int):
        url = f"{self.BASE_URL}/locations/{location_id}/sensors"
        response = requests.get(url, headers=self.headers, params={})
        response.raise_for_status()
        return response.json()["results"]
    
    def get_measurements_by_sensor_id(self, sensor_id: int):
        url = f"{self.BASE_URL}/sensors/{sensor_id}/measurements"
        response = requests.get(url, headers=self.headers, params={})
        response.raise_for_status()
        return response.json()["results"]
