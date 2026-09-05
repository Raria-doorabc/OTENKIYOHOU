import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
print(f"CLIENT_ID: {client_id}")

res=requests.get(f"https://map.yahooapis.jp/weather/V1/place?coordinates=139.6917,35.6895&appid={client_id}&output=json")
print(res.status_code)
print(res.text)
