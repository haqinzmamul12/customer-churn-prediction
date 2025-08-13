import pandas as pd
from src.pipeline import build_pipeline

def test_pipeline_runs():
    df = pd.read_csv(r"./data/customer_churn.csv")
    X = df.drop(columns=['churned', 'customer_id'])
    y = df['churned']

    categorical = ['gender', 'region', 'contract_type']
    date_col = 'signup_date'

    pipeline = build_pipeline(categorical, date_col, numerical_features=[])
    pipeline.fit(X, y)

    preds = pipeline.predict(X)
    assert len(preds) == len(X)
