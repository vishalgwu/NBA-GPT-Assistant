import boto3
import pandas as pd
import time

# AWS configuration
DATABASE   = "nba_curated_db_v2"
OUTPUT_LOC = "s3://nba-analytics-vf-dev/athena/"   # same output folder you used before
REGION     = "us-east-1"

athena = boto3.client("athena", region_name=REGION)

def run_query(query):
    """Run a query in Athena and return a DataFrame."""
    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": OUTPUT_LOC},
    )
    qid = response["QueryExecutionId"]

    # Wait until query finishes
    while True:
        status = athena.get_query_execution(QueryExecutionId=qid)["QueryExecution"]["Status"]["State"]
        if status in ["SUCCEEDED", "FAILED", "CANCELLED"]:
            break
        time.sleep(0.5)

    if status != "SUCCEEDED":
        raise Exception(f"Query failed with status: {status}")

    # Get results
    results = athena.get_query_results(QueryExecutionId=qid)
    columns = [c["VarCharValue"] for c in results["ResultSet"]["Rows"][0]["Data"]]
    rows = [[col.get("VarCharValue", None) for col in r["Data"]] for r in results["ResultSet"]["Rows"][1:]]
    return pd.DataFrame(rows, columns=columns)
