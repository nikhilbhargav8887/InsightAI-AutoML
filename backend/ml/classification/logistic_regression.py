from sklearn.linear_model import LogisticRegression


class LogisticRegressionModel:

    def __init__(self):

        self.model = LogisticRegression(
            max_iter=1000,
            random_state=42
        )

    def train(self, X_train, y_train):

        self.model.fit(
            X_train,
            y_train
        )

    def predict(self, X_test):

        return self.model.predict(
            X_test
        )

    def get_model(self):

        return self.model