import pandas as pd

def prepare_classification_data(df: pd.DataFrame) -> pd.DataFrame:
    # Columnas que serán utilizadas en el modelo
    columns_to_use = [
        'Antiguedad', 'Internauta', 
        'Adicional', 'Dualidad', 'Monoproducto', 'Ctacte', 'Consumo', 'Hipotecario', 
        'Debito', 'Cuentas', 'TC', 'CUPO_L1', 'CUPO_L2', 'CUPO_MX', 'FlgAct_T12', 
        'FlgActCN_T12', 'FlgActCI_T12', 'FlgActAN_T12', 'FlgActAI_T12', 'FlgActPAT_T12', 
        'FlgActCCPC_T12', 'FlgActCCOT_T12', 'FlgActCOL_T12', 'Fac_T12', 'Txs_T12', 
        'FacCN_T12', 'TxsCN_T12', 'FacCI_T12', 'TxsCI_T12', 'FacAN_T12', 'TxsAN_T12', 
        'FacAI_T12', 'TxsAI_T12', 'FacPAT_T12', 'TxsPAT_T12', 'FacCCPC_T12', 'TxsCCPC_T12', 
        'FacCCOT_T12', 'TxsCCOT_T12', 'FacCOL_T12', 'TxsCOL_T12', 'FacDebCom_T12', 
        'TxsDebCom_T12', 'FacDebAtm_T12', 'TxsDebAtm_T12', 'Col_T12', 'ColL1T0_T12', 
        'ColL1TE_T12', 'ColL2T0_T12', 'ColL2AC_T12', 'ColL2CC_T12', 'ColMx_T12', 
        'PagoNac_T12', 'PagoInt_T12', 'EeccNac_T12', 'EeccInt_T12', 'UsoL1_T12', 
        'UsoL2_T12', 'UsoLI_T12', 'target'
    ]
    
    # Filtrar solo las columnas necesarias
    df = df[columns_to_use]
    
    # Convertir las columnas a tipo int donde sea necesario
    for col in df.columns:
        if df[col].dtype == 'float64':
            df[col] = df[col].astype(int)  # Convertir float a int
    
    return df
