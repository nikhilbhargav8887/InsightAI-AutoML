from backend.ml.preprocessing.preprocessor import DataPreprocessor
from backend.ml.preprocessing.feature_splitter import FeatureSplitter
from backend.ml.preprocessing.splitter import TrainTestSplitter


class DataPipeline:

    def prepare_data(self, file_path, target_column):

        preprocessor = DataPreprocessor(file_path)

        preprocessor.load_data()
        preprocessor.remove_duplicates()
        preprocessor.fill_missing_values()
        preprocessor.encode_categorical_columns()

        df = preprocessor.get_dataframe()

        splitter = FeatureSplitter(
            df,
            target_column
        )

        X, y = splitter.split()

        train_splitter = TrainTestSplitter(
            X,
            y
        )

        return train_splitter.split()