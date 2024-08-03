from flask import Flask, request, jsonify
from flask_cors import CORS 
from config import OPENWEATHERMAP_API_KEY
from db import init_db, get_settings_from_db, save_settings_to_db
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app) 

# Initialize the database
init_db()

# Function to fetch weather data from OpenWeatherMap API
def get_weather_from_api(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': location,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_city_name(location):
    weather_data = get_weather_from_api(location)
    if 'city' in weather_data:
        return weather_data['city']['name']
    return "Unknown Location"

# Function to evaluate weather conditions
def evaluate_weather(day, settings):
    temp = day['main']['temp']
    wind_speed = day['wind']['speed']
    rain_chance = day.get('rain', {}).get('3h', 0)  # Use 0 if no rain information
    snow_chance = day.get('snow', {}).get('3h', 0)  # Use 0 if no snow information

    if temp < settings['min_temp'] or temp > settings['max_temp']:
        return False
    if wind_speed > settings['max_wind_speed']:
        return False
    if rain_chance > settings['max_rain_chance']:
        return False
    if snow_chance > settings['max_snow_chance']:
        return False
    
    return True

# Route to get weather data
@app.route('/api/weather/<int:id>', methods=['GET'])
def get_weather(id):
    settings = get_settings_from_db(id)
    if not settings:
        return jsonify({"error": "Settings not found"}), 404

    weather_data = get_weather_from_api(settings['location'])
    city_name = get_city_name(settings['location'])

    response = {
        "id": id,
        "location": settings['location'],
        "city_name": city_name, 
        "departure": settings['departure'],
        "okay_to_bike": []
    }

    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    for day in range(3):
        date = (today + timedelta(days=day)).strftime('%Y-%m-%d')
        bike_okay = False
        for item in weather_data['list']:
            forecast_date = datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if forecast_date == date:
                bike_okay = evaluate_weather(item, settings)
                break
        response['okay_to_bike'].append({
            "date": date,
            "bike_okay": bike_okay
        })

    return jsonify(response)

# Route to save settings
@app.route('/api/weather', methods=['POST'])
def save_settings():
    data = request.json
    new_id = save_settings_to_db(data)
    return jsonify({"id": new_id})

if __name__ == '__main__':
    app.run(debug=True)
