class ModelTrainer:

    def train(
        self,
        model,
        X_train,
        y_train
    ):
        model.train(
            X_train,
            y_train
        )

    def predict(
        self,
        model,
        X_test
    ):
        return model.predict(
            X_test
        )