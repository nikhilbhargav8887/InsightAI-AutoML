class FeatureSplitter:

    def __init__(self, dataframe, target_column):
        self.df = dataframe
        self.target = target_column

    def split(self):

        if self.target not in self.df.columns:
            raise ValueError(
                f"Target column '{self.target}' not found."
            )

        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]

        return X, y