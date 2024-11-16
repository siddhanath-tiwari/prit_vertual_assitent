from app.api_services.weather import get_weather
from app.api_services.news import get_news
from app.utils.text_to_speech import speak

def perform_task(command):
    if "weather" in command:
        city = command.split("in")[-1].strip()
        response = get_weather(city)
    elif "news" in command:
        response = get_news()
    else:
        response = "Sorry, I didn't understand that."
    speak(response)
    return response
