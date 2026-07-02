from sklearn.tree import DecisionTreeClassifier
from backend.ml.classification.base_classifier import BaseClassifier


class DecisionTreeModel(BaseClassifier):

    def __init__(self):
        self.model = DecisionTreeClassifier(
            random_state=42
        )