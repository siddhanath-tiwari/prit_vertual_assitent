import requests
import os

def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url).json()
    if response.get("status") == "ok":
        articles = response["articles"][:5]
        news_list = [f"{article['title']} - {article['source']['name']}" for article in articles]
        return "\n".join(news_list)
    return "Unable to fetch news."