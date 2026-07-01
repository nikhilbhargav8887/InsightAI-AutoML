from sklearn.model_selection import train_test_split


class TrainTestSplitter:

    def __init__(
        self,
        X,
        y,
        test_size=0.2,
        random_state=42
    ):
        self.X = X
        self.y = y
        self.test_size = test_size
        self.random_state = random_state

    def split(self):

        X_train, X_test, y_train, y_test = train_test_split(
            self.X,
            self.y,
            test_size=self.test_size,
            random_state=self.random_state
        )

        return X_train, X_test, y_train, y_test