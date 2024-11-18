import pandas as pd
from sklearn.impute import KNNImputer

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Lista de columnas a eliminar
    columns_to_drop = ['CambioPin', 'Renta']  # Asegúrate de que estas columnas existan en el dataset
    df = df.drop(columns=columns_to_drop, errors='ignore')  # Eliminar columnas
    
    # Lista de columnas categóricas (no convertir a float)
    exclude_columns = ['Sexo', 'IndRev_T12', 'IndRev_T11', 'IndRev_T10', 
                       'IndRev_T09', 'IndRev_T08', 'IndRev_T07', 'IndRev_T06', 
                       'IndRev_T05', 'IndRev_T04', 'IndRev_T03', 'IndRev_T02', 'IndRev_T01']
    
    # Cambiar el tipo de dato a float excepto para las columnas excluidas
    for col in df.columns:
        if col not in exclude_columns:
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                print(f"No se pudo convertir la columna {col} a float.")
    
    # Imputar valores faltantes en columnas categóricas con la moda
    for col in exclude_columns:
        if col in df.columns:
            mode_value = df[col].mode()[0]  # Calcular la moda
            df[col] = df[col].fillna(mode_value)  # Rellenar valores nulos con la moda
    
    # Imputar valores faltantes en columnas numéricas con k-NN
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    block_size = 50
    blocks = [numeric_columns[i:i + block_size] for i in range(0, len(numeric_columns), block_size)]
    for block in blocks:
        imputer = KNNImputer(n_neighbors=3)
        df[block] = pd.DataFrame(imputer.fit_transform(df[block]), columns=block)
    
    return df
