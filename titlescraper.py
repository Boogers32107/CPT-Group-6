import requests
from bs4 import BeautifulSoup
import random

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find_all(["h1", "h2", "h3", "titles", "title", {"class": "title"}])
        title_texts = [title.get_text().strip() for titles in titles]

        return headline_texts if headline_texts else ["No titles found on this page."]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

if __name__ == "__main__":
    url = "https://moxie.foxnews.com/google-publisher/latest.xml"
    titles = scrape_titles(url)
    if titles:
        print(titles)