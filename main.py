from location_api import get_location

city_name = input("天気を知りたい地域を教えてください：")

coordinates = get_location(city_name)
print(coordinates)