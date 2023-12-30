"""
This is a boilerplate pipeline 'model_drift'
generated using Kedro 0.19.1
"""
import os
import logging
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, ClassificationPreset

def model_drift(X_train, X_test, y_train, y_test) -> None:
    try:

        # Data preparation
        reference = pd.concat([X_train, y_train], axis=1)
        current = pd.concat([X_test, y_test], axis=1)

        # Model training
        model = RandomForestClassifier(
            criterion='entropy', 
            max_features=None, 
        )
        model.fit(X_train, y_train)

        # Make predictions
        reference_pred = model.predict(X_train)
        current_pred = model.predict(X_test)

        # Column Mapping
        target = "Satisfaction"
        prediction = "prediction"
        numerical_features = ['Age']
        categorical_features = ['flight_service_1', 'flight_service_2', 'flight_service_3','Gender', 'Customer Type', 'Type of Travel',
                       'Class', 'Flight Distance', 'Departure Delay', 'Arrival Delay', 'Departure and Arrival Time Convenience']
        
        reference['prediction'] = reference_pred
        current['prediction'] = current_pred
        
        column_mapping = ColumnMapping()
        column_mapping.target = target
        column_mapping.prediction = prediction
        column_mapping.numerical_features = numerical_features
        column_mapping.categorical_features = categorical_features

        # Model Performance Report
        classification_performance = Report(metrics=[ClassificationPreset()])      
        classification_performance.run(reference_data=current, current_data=reference,column_mapping=column_mapping)
        classification_performance.show()
        classification_performance.save("data/06_model_drift/model_report.html")

        # Data Drift Report
        data_drift = Report(metrics=[DataDriftPreset()])
        data_drift.run(current_data=reference, reference_data=current, column_mapping=column_mapping)
        data_drift.show()
        data_drift.save("data/06_model_drift/data_drift_report.html")

        # Target Drift Report
        target_drift = Report(metrics=[TargetDriftPreset()])
        target_drift.run(current_data=reference, reference_data=current, column_mapping=column_mapping)
        target_drift.show()
        target_drift.save("data/06_model_drift/target_drift_report.html")

        print("--Model_drift-->  - completed")
        
    except Exception as e:
        logging.error(f"Error occurred in model_drift: {e}")
        raise e





