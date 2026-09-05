import requests
import os
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

load_dotenv()


def get_location(city_name):
    client_id = os.getenv("CLIENT_ID")

    url = "https://map.yahooapis.jp/geocode/cont/V1/contentsGeoCoder"
    params = {
        "query": city_name,
        "appid": client_id,
        "output": "json"
    }
    response = requests.get(url, params=params)
    
    
    print(response.status_code)
    print(response.text)

    data = response.json()
    coordinates = data["Feature"][0]["Geometry"]["Coordinates"]

    longtitude, latitude = coordinates.split(",")

    return longtitude, latitude
