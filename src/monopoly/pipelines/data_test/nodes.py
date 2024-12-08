import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from imblearn.combine import SMOTEENN

def generar_datos_prueba(data: pd.DataFrame):
    # Define the selected features
    selected_features = [
        'FlgActCN_T12', 'FlgActCN_T11', 'FlgActCN_T10', 'FlgActCN_T09', 'FlgActCN_T08',
        'FlgActCN_T07', 'FlgActCN_T06', 'FlgActCN_T05', 'FlgActCN_T04', 'FlgActCN_T03',
        'FlgActCN_T02', 'FlgActCN_T01'
    ]
    
    # Ensure the dataset contains the selected features and the target column
    features = data[selected_features]
    target = data['target']  # Replace 'target' with the actual name of the target column

    # Stratified shuffle split to ensure class distribution in the test set
    stratified_split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for _, test_idx in stratified_split.split(features, target):
        X_test = features.iloc[test_idx]
        y_test = target.iloc[test_idx]

    # Apply SMOTEENN to balance the classes in the test set
    smote_enn = SMOTEENN(random_state=42)
    X_test_balanced, y_test_balanced = smote_enn.fit_resample(X_test, y_test)

    # Convert y_test_balanced to DataFrame for compatibility with Parquet format
    y_test_balanced = pd.DataFrame(y_test_balanced, columns=["target"])  # Name the column as "target"

    return X_test_balanced, y_test_balanced
