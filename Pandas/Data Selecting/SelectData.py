import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Selecciona las filas donde student_id es igual a 101
    result = students.loc[students['student_id'] == 101, ['name', 'age']]
    return result

# Definición del DataFrame students con datos de ejemplo
data = {
    'student_id': [100, 101, 102],
    'name': ['John', 'Alice', 'Bob'],
    'age': [20, 21, 19]
}

students = pd.DataFrame(data)

# Llamada a la función selectData
result = selectData(students)

# Muestra el resultado
print(result)
