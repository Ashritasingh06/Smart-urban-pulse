import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Nagpur"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

print(f"City     : {data['name']}")
print(f"Temp     : {data['main']['temp']}°C")
print(f"Feels    : {data['main']['feels_like']}°C")
print(f"Humidity : {data['main']['humidity']}%")
print(f"Weather  : {data['weather'][0]['description']}")
print(f"Wind     : {data['wind']['speed']} m/s")
print("Done! Live weather fetched from internet.")