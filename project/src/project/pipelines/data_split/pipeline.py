"""
This is a boilerplate pipeline 'data_split'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data_for_evaluation, split_data_for_model_drift


def create_pipeline() -> pipeline:
    return Pipeline([

        node(
            func=split_data_for_evaluation,
            inputs="pre_data",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_for_evaluation_node"
        ),
        node(
            func=split_data_for_model_drift,
            inputs="pre_data",
            outputs=["X_train_drift", "X_test_drift", "y_train_drift", "y_test_drift"],
            name="split_data_for_model_drift_node"
        ),
    ])

def register_pipelines():
    return {
        "data_split": create_pipeline(),
        # Add more pipelines if needed
    }

