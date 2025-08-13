import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DateFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, date_column):
        self.date_column = date_column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.date_column] = pd.to_datetime(X[self.date_column])
        X['signup_month'] = X[self.date_column].dt.month
        X['signup_year'] = X[self.date_column].dt.year
        X = X.drop(columns=[self.date_column])
        return X
