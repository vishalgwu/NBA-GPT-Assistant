import pandas as pd

# Convert players parquet to JSON
players_df = pd.read_parquet("players_cleaned.parquet")
players_df.to_json("players_cleaned.json", orient="records")

# Convert teams parquet to JSON
teams_df = pd.read_parquet("teams_cleaned.parquet")
teams_df.to_json("teams_cleaned.json", orient="records")

print("Conversion completed successfully!")
