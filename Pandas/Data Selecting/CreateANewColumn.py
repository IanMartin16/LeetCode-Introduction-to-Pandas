import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Crear una nueva columna 'bonus' con los valores duplicados de la columna 'salary'
    employees['bonus'] = employees['salary'] * 2
    return employees

# Definición del DataFrame employees con datos de ejemplo
data = {
    'name': ['John', 'Alice', 'Bob'],
    'salary': [50000, 60000, 70000]
}

employees = pd.DataFrame(data)

# Llamada a la función createBonusColumn
result = createBonusColumn(employees)

# Muestra el resultado
print(result)
