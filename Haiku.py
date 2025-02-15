import requests
import random

headline_list = ['Firstword','random', 'uber', 'snake', 'pear', 'frog' ] # Need list of headlines or something Problably from X/Twitter

def generate_haiku():
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = ' '.join(random.choice(headline_list) for _ in range(s))
        haiku.append(line)
    return '\n'.join(haiku)

def post_to_discord(haiku):
   webhook_url = 'https://discord.com/api/webhooks/1339685758273061016/COYZDNyTFckb1PX2PDalu-LUnaea-BEIeQsG9c4ca1my9x2dZTmITiFinjRkjN0Dhini' # I had to add a URL that works for it to not error out just used one for a Server I just created
   payload = { "content": f"Generated Haiku Group 6:\n{haiku}" }
   response = requests.post(webhook_url, json=payload)
   print(response.status_code)
   print("Haiku posted to Discord:")
   print(haiku)


if __name__ == "__main__":
    haiku = generate_haiku()
    post_to_discord(haiku)