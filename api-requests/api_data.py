import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime

url = "https://api.themoviedb.org/3/discover/movie"

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

auth = f"Bearer {API_TOKEN}"

headers = {
    "accept": "application/json",
    "Authorization": auth
}

today = datetime.now().strftime("%Y-%m-%d")

response = requests.get(url, headers=headers)

data = response.json()

for movie in data["results"]:
    movie["ingestion_date"] = today

movies = data["results"]
    
 

with open("./dataset/movie_dataset.json", "w") as file:
    json.dump(movies, file, indent=4)

