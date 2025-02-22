import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_predictive_model():
    # Load data
    data = pd.read_csv('data/equipment_sensor_data.csv')
    X = data[['vibration', 'temperature', 'usage_hours']]
    y = data['failure']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, 'models/predictive_maintenance.pkl')