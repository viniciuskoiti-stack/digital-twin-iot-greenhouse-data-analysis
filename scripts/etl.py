import pandas as pd

def run_etl():
    print("Iniciando ETL...")
    # Carrega dado bruto
    df = pd.read_csv('../data/raw/Advanced_IoT_Dataset.csv')
    
    # Limpeza básica
    df_limpo = df.dropna().drop_duplicates()
    
    # Filtro IQR (Otimizado da M2)
    col_peso = 'Average wet weight of the growth vegetative (AWWGV)'
    Q1 = df_limpo[col_peso].quantile(0.25)
    Q3 = df_limpo[col_peso].quantile(0.75)
    IQR = Q3 - Q1
    
    df_final = df_limpo[(df_limpo[col_peso] >= Q1 - 1.5 * IQR) & 
                        (df_limpo[col_peso] <= Q3 + 1.5 * IQR)]
    
    # Salva na pasta processed
    df_final.to_csv('../data/processed/Advanced_IoT_Dataset_Processed.csv', index=False)
    print("ETL concluído. Dado salvo em /data/processed.")

if __name__ == "__main__":
    run_etl()