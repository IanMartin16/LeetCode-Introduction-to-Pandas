import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Multiplica cada salario por 2
    employees['salary'] = employees['salary'] * 2
    return employees

# Definición del DataFrame employees con datos de ejemplo
data = {
    'name': ['John', 'Alice', 'Bob'],
    'salary': [50000, 60000, 70000]
}

employees = pd.DataFrame(data)

# Llamada a la función modifySalaryColumn
result = modifySalaryColumn(employees)

# Muestra el resultado
print(result)
