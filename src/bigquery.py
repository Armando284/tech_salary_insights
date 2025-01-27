import pandas as pd
from google.cloud import bigquery

def load_to_bigquery(csv_path: str, dataset_id: str, table_id: str) -> None:
    """
    Load a cleaned CSV file into Google BigQuery.

    Args:
        csv_path (str): Path to the cleaned CSV file.
        dataset_id (str): ID of the BigQuery dataset.
        table_id (str): ID of the BigQuery table.
    """
    client = bigquery.Client.from_service_account_json("credentials/tech-salary-insights-9a26b6273124.json")
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = True
    
    with open(csv_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    
    job.result()
    print(f"Data loaded to BigQuery: {dataset_id}.{table_id}")

def query_bigquery(sql_query: str) -> pd.DataFrame:
    """
    Run a SQL query on BigQuery and return results as a Pandas DataFrame.

    Args:
        sql_query (str): SQL query to execute.

    Returns:
        pd.DataFrame: Query results as a Pandas DataFrame.
    """
    client = bigquery.Client.from_service_account_json("credentials/tech-salary-insights-9a26b6273124.json")
    query_job = client.query(sql_query)
    results = query_job.result()

    # Manual conversion to a DataFrame
    rows = [dict(row) for row in results]
    return pd.DataFrame(rows)
