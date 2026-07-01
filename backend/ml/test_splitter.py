from backend.ml.preprocessing.preprocessor import DataPreprocessor
from backend.ml.preprocessing.feature_splitter import FeatureSplitter
from backend.ml.preprocessing.splitter import TrainTestSplitter


preprocessor = DataPreprocessor(
    "datasets/raw/customer_churn.csv"
)

preprocessor.load_data()
preprocessor.remove_duplicates()
preprocessor.fill_missing_values()
preprocessor.encode_categorical_columns()

df = preprocessor.get_dataframe()

splitter = FeatureSplitter(
    df,
    "Churn"
)

X, y = splitter.split()

train_splitter = TrainTestSplitter(X, y)

X_train, X_test, y_train, y_test = train_splitter.split()

print("X Train:", X_train.shape)
print("X Test :", X_test.shape)
print("Y Train:", y_train.shape)
print("Y Test :", y_test.shape)