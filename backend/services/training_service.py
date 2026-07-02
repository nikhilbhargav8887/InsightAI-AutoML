from backend.services.data_pipeline import DataPipeline
from backend.services.automl_service import AutoMLService
from backend.ml.model_selector import ModelSelector
from backend.ml.evaluation.classification_metrics import ClassificationMetrics


class TrainingService:

    def train(self, file_path, target_column):

        pipeline = DataPipeline()

        X_train, X_test, y_train, y_test = pipeline.prepare_data(
            file_path,
            target_column
        )

        automl = AutoMLService().get_engine()

        predictions = automl.train_all(
            X_train,
            y_train,
            X_test
        )

        results = {}

        for model_name, prediction in predictions.items():

            results[model_name] = ClassificationMetrics.evaluate(
                y_test,
                prediction
            )

        selector = ModelSelector()

        best_model = selector.get_best_model(results)

        return {
            "best_model": best_model,
            "metrics": results
        }