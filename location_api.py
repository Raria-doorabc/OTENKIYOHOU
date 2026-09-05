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
    }
    response = requests.get(url, params=params)
    
    root = ET.fromstring(response.text)
    
    print(response.status_code)
    print(response.text)

    namespace = {
        "ydf": "http://olp.yahooapis.jp/ydf/1.0"
    }

    coordinates = root.find(".//ydf:Coordinates", namespace)

    print(coordinates.text)

    longtitude, latitude = coordinates.text.split(",")

    return longtitude, latitude

