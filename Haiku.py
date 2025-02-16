import requests
import random
import re
from headlinescraper import scrape_headlines

def count_syllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        count += 1
    if count == 0:
        count += 1
    return count

def generate_haiku(headline_list):
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = []
        current_syllables = 0
        while current_syllables < s:
            word = random.choice(random.choice(headline_list).split())
            current_syllables += count_syllables(word)
            line.append(word)
            if current_syllables > s:
                line = []
                current_syllables = 0
        haiku.append(' '.join(line))
    return '\n'.join(haiku)

def post_to_discord(haiku):
    webhook_url = 'https://discord.com/api/webhooks/1340312593788829728/MJU1rql7G615JsjkZgLEaE72ujdui3pIgA0kcOFUbGduamLGeCU_vrtjcGBxol0gsYiS'
    payload = { "content": f"Generated Haiku Group 6:\n{haiku}" }
    response = requests.post(webhook_url, json=payload)
    print(response.status_code)
    print("Haiku posted to Discord:")
    print(haiku)

if __name__ == "__main__":
    url = "https://feeds.washingtonpost.com/rss/world"
    headlines = scrape_headlines(url)
    if headlines:
        haiku = generate_haiku(headlines)
        post_to_discord(haiku)
