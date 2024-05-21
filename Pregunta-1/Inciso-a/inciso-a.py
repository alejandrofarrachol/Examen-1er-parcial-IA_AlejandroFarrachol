import csv

# Función para verificar si un valor es numérico
def es_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# Leer el archivo CSV y almacenar los datos numéricos
dataset = []
with open(r'C:\Users\USER\Downloads\00\archivos umsa\U\DAT-245\Examen-1er-parcial-IA_AlejandroFarrachol\Pregunta-1\dataset\sleep.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        # Filtrar y convertir solo los valores numéricos
        datos_fila = [float(valor) if es_numerico(valor) else None for valor in fila]
        dataset.append(datos_fila)

# Número de filas y columnas
num_filas = len(dataset)
num_columnas = len(dataset[0])

# Función para calcular un percentil dado de una lista de valores
def calcular_percentil(lista, percentil):
    # Filtrar valores no numéricos (None)
    lista = [valor for valor in lista if valor is not None]
    if not lista:  # Si la lista está vacía después de filtrar
        return None
    n = len(lista)
    lista_ordenada = sorted(lista)
    pos = (n - 1) * (percentil / 100)
    pos_int = int(pos)
    pos_frac = pos - pos_int
    
    if pos_frac == 0:
        return lista_ordenada[pos_int]
    else:
        return lista_ordenada[pos_int] * (1 - pos_frac) + lista_ordenada[pos_int + 1] * pos_frac

# Extraer las columnas y calcular el percentil 75 y 80 para cada una
percentil_75 = []
percentil_80 = []
for col in range(num_columnas):
    columna = [dataset[fila][col] for fila in range(num_filas)]
    percentil_75.append(calcular_percentil(columna, 75))
    percentil_80.append(calcular_percentil(columna, 80))

print("Percentil 75 de cada columna:", percentil_75)
print("Percentil 80 de cada columna:", percentil_80)
