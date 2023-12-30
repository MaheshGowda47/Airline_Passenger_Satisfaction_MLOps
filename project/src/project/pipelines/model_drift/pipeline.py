"""
This is a boilerplate pipeline 'model_drift'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import model_drift


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=model_drift,
            inputs=["X_train", "X_test", "y_train", "y_test"],
            outputs=None,
        )
    ])