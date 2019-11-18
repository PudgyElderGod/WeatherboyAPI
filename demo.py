import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Peachtree+City&appid=0d6a61287730d18d12a3da6f3408578d"

response = requests.get(weather_url)
response_json = response.json()

main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]

print("It is currently " + str(temp_in_kelvin) + " degrees Kelvin")

temp_in_celsius = (temp_in_kelvin - 273.15)

print("It is currently " + str(temp_in_celsius) + " degrees in Celsius")
