import requests
from dotenv import load_dotenv
import os

url = "https://api.themoviedb.org/3/authentication"

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

auth = f"Bearer {API_TOKEN}"

headers = {
    "accept": "application/json",
    "Authorization": auth
}

response = requests.get(url, headers=headers)

print(response.text)