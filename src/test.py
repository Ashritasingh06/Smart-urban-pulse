import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather?q=Nagpur&appid={API_KEY}&units=metric"
response = requests.get(url)
print(response.json())