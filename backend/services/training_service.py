from backend.ml.preprocessing.preprocessor import DataPreprocessor
from backend.ml.preprocessing.feature_splitter import FeatureSplitter
from backend.ml.preprocessing.splitter import TrainTestSplitter

from backend.ml.classification.random_forest import RandomForestModel

from backend.ml.evaluation.classification_metrics import ClassificationMetrics


class TrainingService:

    def train(self, file_path, target_column):

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

        X_train, X_test, y_train, y_test = train_splitter.split()

        model = RandomForestModel()

        model.train(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        metrics = ClassificationMetrics.evaluate(
            y_test,
            predictions
        )

        return metrics