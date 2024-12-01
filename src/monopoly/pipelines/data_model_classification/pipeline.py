from kedro.pipeline import Pipeline, node
from .nodes import prepare_classification_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=prepare_classification_data,
                inputs="monopoly_clean",  # Dataset limpio como entrada
                outputs="filtered_data",  # Dataset procesado como salida
                name="prepare_classification_data_node",
            ),
        ]
    )
