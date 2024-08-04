import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenar los DataFrames verticalmente
    concatenated_df = pd.concat([df1, df2], ignore_index=True)
    return concatenated_df

# Definición del DataFrame df1 con datos de ejemplo
data1 = {
    'student_id': [1, 2, 3],
    'name': ['John', 'Alice', 'Bob'],
    'age': [20, 21, 22]
}

df1 = pd.DataFrame(data1)

# Definición del DataFrame df2 con datos de ejemplo
data2 = {
    'student_id': [4, 5, 6],
    'name': ['Eve', 'Mallory', 'Trent'],
    'age': [23, 24, 25]
}

df2 = pd.DataFrame(data2)

# Llamada a la función concatenateTables
result = concatenateTables(df1, df2)

# Muestra el resultado
print(result)
