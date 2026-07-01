import pandas as pd


def clean_dataset(file_path):

    df = pd.read_csv(file_path)

    original_rows = len(df)

    missing_values = int(df.isnull().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    df = df.drop_duplicates()

    for column in df.columns:

        if df[column].dtype == "object":
            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

        else:
            df[column] = df[column].fillna(
                df[column].median()
            )

    cleaned_rows = len(df)

    return (
        df,
        {
            "original_rows": original_rows,
            "cleaned_rows": cleaned_rows,
            "missing_values": missing_values,
            "duplicate_rows": duplicate_rows
        }
    )