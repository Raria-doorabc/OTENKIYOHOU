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
    
    data = response.json()
    weather_data = data["Feature"][0]["Property"]["WeatherList"]["Weather"][0]["Rainfall"]
    min60_rainfall = data["Feature"][0]["Property"]["WeatherList"]["Weather"][6]["Rainfall"]

    print(response.status_code)

    return weather_data, min60_rainfall

#print(get_weather("139.6917", "35.6895"))  # Example coordinates for Tokyo