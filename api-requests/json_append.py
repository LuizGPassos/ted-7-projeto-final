import pandas as pd

df = pd.read_json("./dataset/movie_dataset.json")
df.to_csv("./dataset/csv_test.csv")
