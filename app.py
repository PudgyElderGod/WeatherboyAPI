from flask import Flask, render_template, request
import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Peachtree+City&appid=0d6a61287730d18d12a3da6f3408578d"
response = requests.get(weather_url)
response_json = response.json()

main_data = response_json["main"]
temp_in_kelvin = main_data["temp"]
temp_in_celsius = (temp_in_kelvin - 273.15)

print("It is currently " + str(temp_in_celsius) + " degrees in Celsius")

@app.route('/weather')
def weather_form():
    return render_template('weather_form.html')


@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
    params = {
    'appid': API_KEY,
    'q': users_city,
    'units': 'Metric'
    }
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params)
    if not r.status_code == 200:
        print("Something went wrong")
        return render_template('weather_form.html')
    results = r.json()
    city = results['name']
    degrees = results['main']['temp']
    return render_template('weather_results.html', city=city, degrees=degrees)


if __name__ == '__main__':
    app.run()
