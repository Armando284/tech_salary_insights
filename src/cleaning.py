import pandas as pd
from typing import Optional


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load a dataset from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset as a Pandas DataFrame.
    """
    return pd.read_csv(file_path)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean column names by making them lowercase, replacing spaces with underscores, and removing special characters.

    Args:
        df (pd.DataFrame): The original DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with cleaned column names.
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    return df


def drop_missing_values(
    df: pd.DataFrame, threshold: Optional[float] = 0.5
) -> pd.DataFrame:
    """
    Drop columns with a percentage of missing values above a given threshold.

    Args:
        df (pd.DataFrame): The original DataFrame.
        threshold (float, optional): Proportion of missing values allowed before dropping a column. Defaults to 0.5.

    Returns:
        pd.DataFrame: The DataFrame with columns removed based on the threshold.
    """
    # Calculates fraccion of empty values per column
    missing_fraction = df.isnull().mean()

    # Select columns over the threshold
    columns_to_drop = missing_fraction[missing_fraction > threshold].index

    # Remove selected columns
    return df.drop(columns=columns_to_drop)


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values with appropriate defaults (e.g., 0 for numeric columns, 'Unknown' for categorical columns).

    Args:
        df (pd.DataFrame): The original DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(0)
    return df


def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with invalid characters or unrealistic values in the entire dataset.

    Args:
        df (pd.DataFrame): The original DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with invalid rows removed and statistics on rows removed.
    """
    # Track the initial row count
    initial_row_count = len(df)

    # Define a regex pattern to identify invalid characters
    invalid_characters_pattern = r"[^\x20-\x7E]"

    # Remove rows with invalid characters in any column
    for column in df.select_dtypes(include=["object"]).columns:
        df = df[
            ~df[column].str.contains(invalid_characters_pattern, regex=True, na=False)
        ]

    # Remove rows with unrealistic salary values (e.g., salaries above a threshold)
    salary_columns = ["annual_base_pay", "signing_bonus", "annual_bonus"]
    max_salary_threshold = 1e7  # Example threshold: 10 million

    for column in salary_columns:
        if column in df.columns:
            df = df[df[column] <= max_salary_threshold]

    # Track the final row count and calculate rows removed
    final_row_count = len(df)
    rows_removed = initial_row_count - final_row_count

    print(f"Rows removed during cleaning: {rows_removed}")
    return df


def save_cleaned_dataset(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the cleaned DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The cleaned DataFrame.
        output_path (str): Path where the cleaned CSV file will be saved.
    """
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    # Example usage of the cleaning pipeline
    input_file = "data/raw/tech_salaries.csv"
    output_file = "data/processed/cleaned_tech_salaries.csv"

    # Load the dataset
    data = load_dataset(input_file)

    # Clean the dataset
    data = clean_column_names(data)
    data = drop_missing_values(data, threshold=0.5)
    data = fill_missing_values(data)
    data = remove_invalid_rows(data)

    # Save the cleaned dataset
    save_cleaned_dataset(data, output_file)
