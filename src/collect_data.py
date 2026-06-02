import requests
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Nagpur"
LAT = 21.1458
LON = 79.0882

aqi_levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    return {
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "weather": data['weather'][0]['description']
    }

def fetch_aqi():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
    data = requests.get(url).json()
    aqi = data['list'][0]['main']['aqi']
    components = data['list'][0]['components']
    return {
        "aqi": aqi,
        "aqi_label": aqi_levels[aqi],
        "pm2_5": components['pm2_5'],
        "pm10": components['pm10'],
        "co": components['co'],
        "no2": components['no2']
    }

def save_to_csv(row):
    file = "data/city_data.csv"
    file_exists = os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print(f"✅ Data saved to {file}")

# Collect everything
print("Fetching data...")
weather = fetch_weather()
aqi = fetch_aqi()

row = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "city": CITY,
    **weather,
    **aqi
}

print(f"Temp: {row['temperature']}°C | AQI: {row['aqi_label']} | PM2.5: {row['pm2_5']}")
save_to_csv(row)