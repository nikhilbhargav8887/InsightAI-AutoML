from backend.ml.model_registry import ModelRegistry
from backend.ml.trainer import ModelTrainer


class AutoMLEngine:

    def __init__(self):

        self.registry = ModelRegistry()
        self.trainer = ModelTrainer()

    def register_model(self, model):

        self.registry.register(model)

    def get_models(self):

        return self.registry.get_models()

    def train_all(
        self,
        X_train,
        y_train,
        X_test
    ):

        predictions = {}

        for model in self.registry.get_models():

            self.trainer.train(
                model,
                X_train,
                y_train
            )

            predictions[
                model.__class__.__name__
            ] = self.trainer.predict(
                model,
                X_test
            )

        return predictions