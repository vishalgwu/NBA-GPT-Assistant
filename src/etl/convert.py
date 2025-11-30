import pandas as pd

# Convert players parquet → JSON
players_df = pd.read_parquet("players_cleaned.parquet")
players_df.to_json("players_cleaned.json", orient="records")
print("players_cleaned.json created")

# Convert teams parquet → JSON
teams_df = pd.read_parquet("teams_cleaned.parquet")
teams_df.to_json("teams_cleaned.json", orient="records")
print("teams_cleaned.json created")

print("All conversions completed successfully!")

