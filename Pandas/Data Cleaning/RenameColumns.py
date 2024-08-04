import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Renombrar las columnas
    students = students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'student_age'
    })
    return students

# Definición del DataFrame students con datos de ejemplo
data = {
    'id': [1, 2, 3],
    'first': ['John', 'Alice', 'Bob'],
    'last': ['Doe', 'Smith', 'Johnson'],
    'age': [20, 21, 22]
}

students = pd.DataFrame(data)

# Llamada a la función renameColumns
result = renameColumns(students)

# Muestra el resultado
print(result)
