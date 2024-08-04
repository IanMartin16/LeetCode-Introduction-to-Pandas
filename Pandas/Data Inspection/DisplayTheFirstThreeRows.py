import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Mostrar las primeras 3 filas del DataFrame employees
    return employees.head(3)

# Definición del DataFrame employees
data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

employees = pd.DataFrame(data)

# Llamada a la función selectFirstRows
first_three_rows = selectFirstRows(employees)

# Muestra el resultado
print(first_three_rows)
