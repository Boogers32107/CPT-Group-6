import time
import requests
import random

def generate_haiku():
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = ' '.join(random.choice() for _ in range(s)) #We need a API or something
        haiku.append(line)
    return '\n'.join(haiku)

def post_to_discord(haiku):
    webhook_url = "Teacher will provide webhook"
    payload = {
        "content": haiku
    }
    response = requests.post(webhook_url, json=payload)
    print(response.status_code)

if __name__ "__main__":
api_key = "We NEED and API"
