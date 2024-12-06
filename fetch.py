import requests

def fetch_jokes_from_api(amount):
    url = f"https://v2.jokeapi.dev/joke/Any?amount={amount}"
    response = requests.get(url)
    response.raise_for_status()  
    return response.json()
    

