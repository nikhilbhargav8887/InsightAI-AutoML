from sklearn.neighbors import KNeighborsClassifier
from backend.ml.classification.base_classifier import BaseClassifier


class KNNModel(BaseClassifier):

    def __init__(self):
        self.model = KNeighborsClassifier(
            n_neighbors=5
        )