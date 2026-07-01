import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataPreprocessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    # Convert TotalCharges to numeric
        if "TotalCharges" in self.df.columns:
          self.df["TotalCharges"] = pd.to_numeric(
                   self.df["TotalCharges"],
               errors="coerce"
        )
          
        return self.df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def fill_missing_values(self):

        for column in self.df.columns:

            if pd.api.types.is_numeric_dtype(self.df[column]):
                self.df[column] = self.df[column].fillna(
                    self.df[column].median()
                )

            else:
                self.df[column] = self.df[column].fillna(
                    self.df[column].mode()[0]
                )

    def encode_categorical_columns(self):

        encoder = LabelEncoder()

        for column in self.df.select_dtypes(include="object").columns:
            self.df[column] = encoder.fit_transform(
                self.df[column]
            )

    def get_dataframe(self):
        return self.df
