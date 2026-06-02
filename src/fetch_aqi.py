import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Nagpur coordinates
LAT = 21.1458
LON = 79.0882

# Fetch Air Quality data
url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
response = requests.get(url)
data = response.json()

# AQI level meanings
aqi_levels = {1: "Good", 2: "Fair", 3: "Moderate", 4: "Poor", 5: "Very Poor"}

aqi = data['list'][0]['main']['aqi']
components = data['list'][0]['components']

print(f"City        : Nagpur")
print(f"AQI Level   : {aqi} - {aqi_levels[aqi]}")
print(f"PM2.5       : {components['pm2_5']} μg/m³")
print(f"PM10        : {components['pm10']} μg/m³")
print(f"CO          : {components['co']} μg/m³")
print(f"NO2         : {components['no2']} μg/m³")
print("✅ AQI data fetched successfully!")