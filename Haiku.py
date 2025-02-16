import requests
import random
import re
from titlescraper import scrape_titles

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

def generate_haiku(titles_list):
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = []
        current_syllables = 0
        while current_syllables < s:
            word = random.choice(random.choice(titles_list).split())
            current_syllables += count_syllables(word)
            line.append(word)
            if current_syllables > s:
                line = []
                current_syllables = 0
        haiku.append(' '.join(line))
    return '\n'.join(haiku)

def post_to_discord(haiku):
    webhook_url = 'https://discord.com/api/webhooks/1339685758273061016/COYZDNyTFckb1PX2PDalu-LUnaea-BEIeQsG9c4ca1my9x2dZTmITiFinjRkjN0Dhini'
    payload = { "content": f"Generated Haiku Group 6:\n{haiku}" }
    response = requests.post(webhook_url, json=payload)
    print(response.status_code)
    print("Haiku posted to Discord:")
    print(haiku)

if __name__ == "__main__":
    url = "https://feeds.washingtonpost.com/rss/world"
    titles = scrape_titles(url)
    if titles:
        haiku = generate_haiku(titles)
        post_to_discord(haiku)
