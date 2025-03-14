import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from termcolor import colored

url = "https://api.themoviedb.org/3/discover/movie"

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

auth = f"Bearer {API_TOKEN}"

headers = {
    "accept": "application/json",
    "Authorization": auth
}

today = datetime.now().strftime("%Y-%m-%d")

movies = []
total_pages = 500

for page in range(1, total_pages + 1):
    try:
        params = {
            "page": page
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        for movie in data.get("results", []):
            movie["ingestion_date"] = today
            movies.append(movie)
        print(colored(f"Página {page} inserida com sucesso!", "green"))
    except:
        print(colored(f"Erro ao inserir página.", "red"))
with open("./dataset/movie_dataset.json", "w") as file:
    json.dump(movies, file, indent=4)
