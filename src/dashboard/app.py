import streamlit as st
from query_athena import run_query
import pandas as pd

st.set_page_config(page_title="NBA Analytics Dashboard", layout="wide")
st.title("🏀 NBA Analytics Dashboard (AWS Athena + S3)")

# Tabs for different views
tab1, tab2 = st.tabs(["Players", "Teams"])

with tab1:
    st.subheader("Active Players Count")
    df = run_query("""
        SELECT date, COUNT(*) AS active_players
        FROM players_cleaned
        WHERE is_active = true
        GROUP BY date
        ORDER BY date DESC;
    """)
    st.dataframe(df)

    st.subheader("Sample Players Data")
    st.dataframe(run_query("SELECT * FROM players_cleaned LIMIT 10;"))

with tab2:
    st.subheader("Teams List")
    st.dataframe(run_query("SELECT * FROM teams_cleaned LIMIT 10;"))

st.caption("Data source: NBA API → AWS S3 → Glue → Athena → Streamlit")
