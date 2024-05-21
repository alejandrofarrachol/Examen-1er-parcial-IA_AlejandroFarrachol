import pandas as pd
import numpy as np

# Ubicación del archivo CSV
ruta_archivo_pd = r'C:\Users\USER\Downloads\00\archivos umsa\U\DAT-245\Examen-1er-parcial-IA_AlejandroFarrachol\Pregunta-1\dataset\sleep.csv'

# Utilizando Pandas para leer el archivo CSV y crear un DataFrame
data_pd = pd.read_csv(ruta_archivo_pd)

# Codificar las columnas no numéricas utilizando one-hot encoding
data_pd_encoded = pd.get_dummies(data_pd, columns=['columna_no_numerica'])

# Convertir DataFrame de Pandas a NumPy array
data_np = data_pd_encoded.to_numpy()

# Calcular percentiles de NumPy
percentil_75_np = np.percentile(data_np, 75, axis=0)
percentil_80_np = np.percentile(data_np, 80, axis=0)

# Mostrar los resultados
print("Percentil 75 (NumPy):", percentil_75_np)
print("Percentil 80 (NumPy):", percentil_80_np)
