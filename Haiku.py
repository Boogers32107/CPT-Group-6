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
            phrase = random.choice(headline_list).split(" ")
            phrase = random.choice(phrase)
            phrase_words = phrase.split()
            phrase_syllables = sum(count_syllables(word) for word in phrase_words)
            if current_syllables + phrase_syllables <= s:
                current_syllables += phrase_syllables
                line.extend(phrase_words)
            else:
                continue
        
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
    url = "https://moxie.foxnews.com/google-publisher/latest.xml"
    headlines = scrape_headlines(url)
    if headlines:
        haiku = generate_haiku(headlines)
        post_to_discord(haiku)
