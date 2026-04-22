from flask import Flask, render_template
from weather import fetch_all_cities
from database import save_weather, get_history
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    weather_data = fetch_all_cities()
    
    # Save each city reading to database
    for data in weather_data:
        save_weather(data)
    
    return render_template("index.html", weather=weather_data)

@app.route("/history/<city>")
def history(city):
    readings = get_history(city)
    return render_template("history.html", city=city, readings=readings)

@app.route("/health")
def health():
    return {"status": "ok", "message": "PacificWeather Hub is running!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)