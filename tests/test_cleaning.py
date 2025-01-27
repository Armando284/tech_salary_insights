import pytest
import pandas as pd
from cleaning import (
    clean_column_names,
    drop_missing_values,
    fill_missing_values,
    remove_invalid_rows,
    load_dataset,
    save_cleaned_dataset,
)


@pytest.fixture
def sample_dataframe():
    """Fixture for a sample DataFrame to test with."""
    data = {
        "Column A": [1, 2, None, 4],
        "Column B": ["A", "B", "C", "D"],
        "Column C": [None, None, None, "Unknown"],
        "annual_base_pay": [50000, 60000, 1e9, 70000],  # 1e9 it's an unrealistic value
        "signing_bonus": [1000, 2000, None, 4000],  # Additional test column
        "invalid_col": ["valid", "valid", "invalid\x00", "valid"],  # Invalid character
    }
    return pd.DataFrame(data)


def test_clean_column_names(sample_dataframe):
    """Test that column names are cleaned correctly."""
    df = clean_column_names(sample_dataframe)
    expected_columns = [
        "column_a",
        "column_b",
        "column_c",
        "annual_base_pay",
        "signing_bonus",
        "invalid_col",
    ]
    assert list(df.columns) == expected_columns


def test_drop_missing_values(sample_dataframe):
    """Test that columns with high missing values are dropped."""
    df = clean_column_names(sample_dataframe)  # Clean column names first
    df = drop_missing_values(df, threshold=0.5)
    assert "column_c" not in df.columns  # 'column_c' it's 75% null
    assert "column_a" in df.columns  # 'column_a' it's only 25% null


def test_fill_missing_values(sample_dataframe):
    """Test that missing values are filled appropriately."""
    df = clean_column_names(sample_dataframe)  # Clean column name first
    df = fill_missing_values(df)

    # Check null values at columns are defaulted to 0
    assert df["column_a"].isnull().sum() == 0
    assert df["signing_bonus"].isnull().sum() == 0

    # Check string columns are defaulted to 'Unknown'
    assert df["column_c"].isnull().sum() == 0
    assert df["column_c"].iloc[0] == "Unknown"


def test_remove_invalid_rows(sample_dataframe):
    """Test that rows with invalid characters or unrealistic salaries are removed."""
    df = clean_column_names(sample_dataframe)
    df = remove_invalid_rows(df)

    # Check no rows with invalid characters
    assert (
        df["invalid_col"].str.contains(r"[^\x20-\x7E]", regex=True, na=False).sum() == 0
    )

    # Check no unrealistic salaries
    assert df["annual_base_pay"].max() <= 1e7

    # Check wrong rows were deleted
    assert len(df) < len(sample_dataframe)


def test_load_dataset(tmp_path):
    """Test that a dataset is loaded correctly from a CSV file."""
    # Create temporary csv file
    file_path = tmp_path / "test_data.csv"
    sample_data = {"col1": [1, 2, 3], "col2": ["A", "B", "C"]}
    pd.DataFrame(sample_data).to_csv(file_path, index=False)

    # Load csv file
    df = load_dataset(file_path)

    # Check data correctly loaded
    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 3


def test_save_cleaned_dataset(tmp_path):
    """Test that a cleaned dataset is saved correctly to a CSV file."""
    # Create test DataFrame
    sample_data = {"col1": [1, 2, 3], "col2": ["A", "B", "C"]}
    df = pd.DataFrame(sample_data)

    # Save DataFrame to CSV file
    output_path = tmp_path / "cleaned_data.csv"
    save_cleaned_dataset(df, output_path)

    # Checks file saved correctly
    assert output_path.exists()
    loaded_df = pd.read_csv(output_path)
    assert loaded_df.equals(df)


if __name__ == "__main__":
    pytest.main()
