import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from termcolor import colored

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

base_url = "https://api.themoviedb.org/3"

auth = f"Bearer {API_TOKEN}"

headers = {
    "accept": "application/json",
    "Authorization": auth
}

today = datetime.now().strftime("%Y-%m-%d")

movies = []

discover_url = f"{base_url}/discover/movie"
total_pages = 30

movie_ids = []

for page in range(1, total_pages + 1):
    try:
        params = {"page": page}
        response = requests.get(discover_url, headers=headers, params=params)
        data = response.json()

        for movie in data.get("results", []):
            movie_ids.append(movie["id"])

        print(f"IDs da página {page} coletados com {colored("sucesso", "green")}!")
    except Exception as e:
        print(f"{colored("Erro", "red")} ao coletar IDs na página {page}: {e}")


for movie_id in movie_ids:
    try:
        movie_url = f"{base_url}/movie/{movie_id}?language=en-US"
        response = requests.get(movie_url, headers=headers)
        movie_details = response.json()

        movie_details["ingestion_date"] = today
        movies.append(movie_details)

        print(f"Detalhes do filme {movie_id} coletados com {colored("sucesso", "green")}!")
    except Exception as e:
        print(f"{colored("Erro", "red")} ao coletar detalhes do filme {movie_id}: {e}")


with open("./dataset/movie_dataset.json", "w") as file:
    json.dump(movies, file, indent=4)

print(colored("Coleta de detalhes dos filmes concluída!", "blue"))
