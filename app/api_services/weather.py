import requests
import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    if response.get("cod") == 200:
        weather = response["weather"][0]["description"]
        temp = response["main"]["temp"] - 273.15
        return f"The weather in {city} is {weather} with a temperature of {temp:.2f}°C."
    return "City not found."
