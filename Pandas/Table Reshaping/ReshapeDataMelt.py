import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Usar la función melt para transformar el DataFrame
    reshaped = pd.melt(report, id_vars=['product'], 
                       var_name='quarter', 
                       value_name='sales')
    return reshaped

# Ejemplo de uso
data = {
    'product': ['A', 'B', 'C'],
    'quarter_1': [100, 150, 200],
    'quarter_2': [110, 160, 210],
    'quarter_3': [120, 170, 220],
    'quarter_4': [130, 180, 230]
}
report = pd.DataFrame(data)

reshaped_report = meltTable(report)
print(reshaped_report)
