from sklearn.svm import SVC
from backend.ml.classification.base_classifier import BaseClassifier


class SVMModel(BaseClassifier):

    def __init__(self):
        self.model = SVC(
            probability=True,
            random_state=42
        )