import pandas as pd


def analyze_dataset(file_path):

    df = pd.read_csv(file_path)

    analysis = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),

        "numerical_columns": list(
            df.select_dtypes(include=["number"]).columns
        ),

        "categorical_columns": list(
            df.select_dtypes(include=["object"]).columns
        ),

        "missing_values": (
            df.isnull()
            .sum()
            .to_dict()
        ),

        "data_types": (
            df.dtypes
            .astype(str)
            .to_dict()
        ),

        "summary_statistics": (
            df.describe(include="all")
            .fillna("")
            .to_dict()
        )
    }

    return analysis