import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Elimina las filas donde hay valores faltantes en la columna 'name'
    students = students.dropna(subset=['name'])
    return students

# Definición del DataFrame students con datos de ejemplo, incluyendo algunos valores faltantes
data = {
    'student_id': [1, 2, 3, 4],
    'name': ['John', None, 'Alice', 'Bob'],
    'age': [20, 21, 22, 23]
}

students = pd.DataFrame(data)

# Llamada a la función dropMissingData
result = dropMissingData(students)

# Muestra el resultado
print(result)
