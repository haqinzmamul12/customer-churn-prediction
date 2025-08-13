import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.pipeline import build_pipeline
from src.logger import logging 
from sklearn.metrics import classification_report

import os 
import sys 

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def predict(input_df):
    logging.info("Loading the dataset!")
    df = pd.read_csv(r"./data/customer_churn.csv")

    X = df.drop(columns=['Names', 'Churn'])
    y = df['Churn']

    date_column = 'Onboard_date'
    categorical_features = [feature for feature in X.columns if X[feature].dtype=='object' and feature!=date_column]
    numerical_features = X.columns[~X.columns.isin(categorical_features + [date_column])].to_list()

    logging.info("Splitting the dataset!")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    logging.info("Running Pre-processing pipelines!")
    pipeline = build_pipeline(categorical_features, date_column, numerical_features)

    logging.info("training the model!")
    pipeline.fit(X_train, y_train)

    y_pred =pipeline.predict(X_test)
    report =classification_report(y_test, y_pred)
    print(f"Classification Report:")
    print(report)
    return pipeline.predict(input_df)

