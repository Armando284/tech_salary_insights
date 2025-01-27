from google.cloud import bigquery
import os

def load_to_bigquery(csv_path: str, dataset_id: str, table_id: str) -> None:
    """
    Load a cleaned CSV file into Google BigQuery.

    Args:
        csv_path (str): Path to the cleaned CSV file.
        dataset_id (str): ID of the BigQuery dataset.
        table_id (str): ID of the BigQuery table.
    """
    # Configure BigQuery client
    client = bigquery.Client.from_service_account_json("credentials/tech-salary-insights-9a26b6273124.json")
    
    # Configure table ref
    table_ref = client.dataset(dataset_id).table(table_id)
    
    # Configure load job
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = True  # BigQuery will automatically detect schema
    
    # load CSV
    with open(csv_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    
    job.result()  # wait job finish
    print(f"Datos cargados en BigQuery: {dataset_id}.{table_id}")

if __name__ == "__main__":
    csv_path = "data/processed/cleaned_tech_salaries.csv"
    dataset_id = "tech_salaries_dataset"  # Change by dataset ID
    table_id = "cleaned_salaries"  # Change by table ID
    load_to_bigquery(csv_path, dataset_id, table_id)