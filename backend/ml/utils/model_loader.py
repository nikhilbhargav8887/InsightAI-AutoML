import joblib
from pathlib import Path


class ModelLoader:

    MODEL_DIR = Path("models")

    @classmethod
    def load(cls, filename):

        filepath = cls.MODEL_DIR / filename

        model = joblib.load(filepath)

        return model