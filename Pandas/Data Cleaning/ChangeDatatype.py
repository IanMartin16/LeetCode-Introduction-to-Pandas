import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Convertir la columna 'grade' de flotantes a enteros
    students['grade'] = students['grade'].astype(int)
    return students

# Definición del DataFrame students con datos de ejemplo
data = {
    'student_id': [1, 2, 3],
    'name': ['John', 'Alice', 'Bob'],
    'age': [20, 21, 22],
    'grade': [88.5, 92.3, 85.0]
}

students = pd.DataFrame(data)

# Llamada a la función changeDatatype
result = changeDatatype(students)

# Muestra el resultado
print(result)
