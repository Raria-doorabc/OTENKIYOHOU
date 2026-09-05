from location_api import get_location
from weather_api import get_weather

city_name = input("天気を知りたい地域を教えてください：")

coordinates = get_location(city_name)
print(coordinates)
weather_data, min60_rainfall = get_weather(*coordinates)
print(f"現在の天気: {weather_data}")
print(f"60分後の雨量: {min60_rainfall}")
