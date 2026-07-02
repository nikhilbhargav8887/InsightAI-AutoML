from backend.ml.automl import AutoMLEngine

from backend.ml.classification.random_forest import RandomForestModel
from backend.ml.classification.logistic_regression import LogisticRegressionModel
from backend.ml.classification.decision_tree import DecisionTreeModel
from backend.ml.classification.knn import KNNModel
from backend.ml.classification.svm import SVMModel


class AutoMLService:

    def __init__(self):

        # Create the AutoML engine FIRST
        self.automl = AutoMLEngine()

        # Register all models
        self.automl.register_model(RandomForestModel())
        self.automl.register_model(LogisticRegressionModel())
        self.automl.register_model(DecisionTreeModel())
        self.automl.register_model(KNNModel())
        self.automl.register_model(SVMModel())

    def get_engine(self):

        return self.automl