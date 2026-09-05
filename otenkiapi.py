import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(longitude, latitude):
    client_id = os.getenv("CLIENT_ID")
    url = "https://map.yahooapis.jp/weather/V1/place"
    params = {
        "coordinates": f"{longitude},{latitude}",
        "appid": client_id,
        "output": "json"
    }
    response = requests.get(url, params=params)

    print(response.status_code)
    print(response.text)
