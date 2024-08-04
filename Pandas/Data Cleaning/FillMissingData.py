import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Rellenar los valores faltantes en la columna 'quantity' con 0
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Definición del DataFrame products con datos de ejemplo, incluyendo valores faltantes en la columna 'quantity'
data = {
    'name': ['Product1', 'Product2', 'Product3'],
    'quantity': [10, None, 5],
    'price': [100, 150, 200]
}

products = pd.DataFrame(data)

# Llamada a la función fillMissingValues
result = fillMissingValues(products)

# Muestra el resultado
print(result)
