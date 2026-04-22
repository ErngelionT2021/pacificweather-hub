import requests
import os

# Pacific Island cities
PACIFIC_CITIES = [
    {"name": "Honiara",    "country": "SB", "lat": -9.43,  "lon": 160.05},
    {"name": "Apia",       "country": "WS", "lat": -13.83, "lon": -171.77},
    {"name": "Suva",       "country": "FJ", "lat": -18.14, "lon": 178.44},
    {"name": "Port Vila",  "country": "VU", "lat": -17.73, "lon": 168.32},
    {"name": "Nukualofa",  "country": "TO", "lat": -21.13, "lon": -175.20},
]

def fetch_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": city["lat"],
        "lon": city["lon"],
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return {
        "city":        city["name"],
        "country":     city["country"],
        "temp":        data["main"]["temp"],
        "humidity":    data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind_speed":  data["wind"]["speed"],
    }

def fetch_all_cities():
    return [fetch_weather(city) for city in PACIFIC_CITIES]