import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Elimina las filas duplicadas basadas en la columna 'email', manteniendo solo la primera ocurrencia
    customers = customers.drop_duplicates(subset='email', keep='first')
    return customers

# Definición del DataFrame customers con datos de ejemplo
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Alice', 'John'],
    'email': ['john@example.com', 'alice@example.com', 'bob@example.com', 'alice@example.com', 'john@example.com']
}

customers = pd.DataFrame(data)

# Llamada a la función dropDuplicateEmails
result = dropDuplicateEmails(customers)

# Muestra el resultado
print(result)
