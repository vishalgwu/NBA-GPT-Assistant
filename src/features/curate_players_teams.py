import os
import pandas as pd
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# Base data dir: src/etl/data (relative to src/features)
BASE_DATA_DIR = os.path.join("..", "etl", "data")

today = date.today().isoformat()

# ----- RAW PATHS -----
raw_dir = os.path.join(BASE_DATA_DIR, "raw", today)

players_raw_path = os.path.join(raw_dir, "players.parquet")
teams_raw_path   = os.path.join(raw_dir, "teams.parquet")

# ----- CURATED PATHS (BETTER STRUCTURE) -----
players_curated_dir = os.path.join(
    BASE_DATA_DIR, "curated", "players_cleaned", f"date={today}"
)
teams_curated_dir = os.path.join(
    BASE_DATA_DIR, "curated", "teams_cleaned", f"date={today}"
)

os.makedirs(players_curated_dir, exist_ok=True)
os.makedirs(teams_curated_dir, exist_ok=True)

players_curated_path = os.path.join(players_curated_dir, "players_cleaned.parquet")
teams_curated_path   = os.path.join(teams_curated_dir, "teams_cleaned.parquet")

# ----- LOAD RAW DATA -----
players_df = pd.read_parquet(players_raw_path)
teams_df   = pd.read_parquet(teams_raw_path)

# ----- CLEAN PLAYERS -----
players_cleaned = players_df[["id", "full_name", "is_active"]].rename(
    columns={"id": "player_id", "full_name": "player_name"}
)

# ----- CLEAN TEAMS -----
teams_cleaned = teams_df[["id", "full_name"]].rename(
    columns={"id": "team_id", "full_name": "team_name"}
)

# ----- WRITE CURATED FILES -----
players_cleaned.to_parquet(players_curated_path, index=False)
teams_cleaned.to_parquet(teams_curated_path, index=False)

print("✅ Wrote players to:", players_curated_path)
print("✅ Wrote teams   to:", teams_curated_path)
