import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# 1. Carga do dado PROCESSADO
df = pd.read_csv('../data/processed/Advanced_IoT_Dataset_Processed.csv')

X = df[['Average  of chlorophyll in the plant (ACHP)', 'Plant height rate (PHR)', 'Average leaf area of the plant (ALAP)', 'Average number of plant leaves (ANPL)']]
y = df['Average wet weight of the growth vegetative (AWWGV)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Modelo com os Melhores Hiperparâmetros da M4
modelo = RandomForestRegressor(
    max_depth=10, 
    min_samples_split=10, 
    n_estimators=150, 
    random_state=42
)

modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# 3. Métricas
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("--- MODELO OTIMIZADO (M4) TREINADO ---")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R2: {modelo.score(X_test, y_test)*100:.2f}%")