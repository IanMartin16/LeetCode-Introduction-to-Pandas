import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivotar el DataFrame para que cada fila represente las temperaturas de un mes específico y cada ciudad sea una columna separada
    pivoted_df = weather.pivot(index='month', columns='city', values='temperature')
    return pivoted_df

# Definición del DataFrame weather con datos de ejemplo
data = {
    'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'month': ['January', 'January', 'February', 'February', 'March', 'March'],
    'temperature': [30, 60, 32, 65, 50, 70]
}

weather = pd.DataFrame(data)

# Llamada a la función pivotTable
result = pivotTable(weather)

# Muestra el resultado
print(result)
