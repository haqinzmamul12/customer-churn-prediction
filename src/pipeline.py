from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from category_encoders import TargetEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from src.processing import DateFeatureExtractor

def build_pipeline(categorical_features, date_column, numerical_features):
    preprocessing = ColumnTransformer([
        ('target_encode', TargetEncoder(), categorical_features),
        ('date_features', DateFeatureExtractor(date_column), [date_column]),
        ('scale', StandardScaler(), numerical_features)
    ])

    pipeline = Pipeline([
        ('preprocess', preprocessing),
        #('model', RandomForestClassifier(n_estimators=50, random_state=42))
        ('model', LogisticRegression(max_iter=5000, solver='saga'))
    ])
    return pipeline
