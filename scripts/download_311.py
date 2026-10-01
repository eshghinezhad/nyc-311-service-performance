import requests, pandas as pd

URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"
params = {
       "$where": "created_date between '2025-01-01T00:00:00' and '2025-01-31T23:59:59'",
       "$limit": 10000,
   }
r = requests.get(URL, params=params)
r.raise_for_status()
open("data/raw/sample_311.csv", "wb").write(r.content)
print(pd.read_csv("data/raw/sample_311.csv").shape)