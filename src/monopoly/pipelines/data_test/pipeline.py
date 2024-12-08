from kedro.pipeline import Pipeline, node
from .nodes import generar_datos_prueba

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            generar_datos_prueba,
            inputs="monopoly_clean",  # Input dataset
            outputs=["X_test_balanced", "y_test_balanced"],  # Outputs for balanced test data
            name="generar_datos_prueba"
        )
    ])
