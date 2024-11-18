from kedro.pipeline import Pipeline, node
from .nodes import clean_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs="monopoly",  # Este nombre debe coincidir con el del catalog.yml
                outputs="monopoly_clean",  # Este también debe coincidir
                name="clean_data_node",
            ),
        ]
    )
