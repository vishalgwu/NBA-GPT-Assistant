# src/etl/ingest_nba.py
import os
import pandas as pd
from datetime import date
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "./data")

today = date.today().isoformat()
raw_dir = os.path.join(DATA_DIR, "raw", today)
curated_dir = os.path.join(DATA_DIR, "curated", f"date={today}")
os.makedirs(curated_dir, exist_ok=True)


def main():
    today = date.today().isoformat()
    raw_dir = os.path.join(DATA_DIR, "raw", today)
    os.makedirs(raw_dir, exist_ok=True)

    # Fetch simple datasets
    players_df = pd.DataFrame(players.get_players())
    teams_df = pd.DataFrame(teams.get_teams())

    players_df.to_parquet(os.path.join(raw_dir, "players.parquet"))
    teams_df.to_parquet(os.path.join(raw_dir, "teams.parquet"))

    print(f" Data saved successfully at: {raw_dir}")

if __name__ == "__main__":
    main()
