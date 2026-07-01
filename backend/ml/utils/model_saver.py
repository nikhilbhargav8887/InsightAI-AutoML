import joblib
from pathlib import Path


class ModelSaver:

    MODEL_DIR = Path("models")

    @classmethod
    def save(cls, model, filename):

        cls.MODEL_DIR.mkdir(
            exist_ok=True
        )

        filepath = cls.MODEL_DIR / filename

        joblib.dump(
            model,
            filepath
        )

        return filepath