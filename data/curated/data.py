import pandas as pd

# Players
players_df = pd.read_parquet("players_cleaned.parquet", engine="fastparquet")
players_df.to_json("players_cleaned.json", orient="records")

# Teams
teams_df = pd.read_parquet("teams_cleaned.parquet", engine="fastparquet")
teams_df.to_json("teams_cleaned.json", orient="records")

print("JSON files created!")
