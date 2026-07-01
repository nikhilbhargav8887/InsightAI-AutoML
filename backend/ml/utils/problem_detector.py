import pandas as pd


def detect_problem(df, target_column):

    target = df[target_column]

    # Numeric target
    if pd.api.types.is_numeric_dtype(target):

        unique_values = target.nunique()

        # Few unique values → Classification
        if unique_values <= 10:
            return "classification"

        # Many unique values → Regression
        return "regression"

    # String/Object target
    return "classification"