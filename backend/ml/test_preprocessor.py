from backend.ml.preprocessing.preprocessor import DataPreprocessor

preprocessor = DataPreprocessor(
    "datasets/raw/customer_churn.csv"
)

preprocessor.load_data()

preprocessor.remove_duplicates()

preprocessor.fill_missing_values()

preprocessor.encode_categorical_columns()

df = preprocessor.get_dataframe()

print(df.head())

print("\nShape:", df.shape)