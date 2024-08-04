import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filtrar animales que pesan más de 100 kilogramos
    heavy_animals = animals[animals['weight'] > 100]
    
    # Ordenar por peso en orden descendente
    heavy_animals_sorted = heavy_animals.sort_values(by='weight', ascending=False)
    
    # Seleccionar solo la columna 'name'
    result = heavy_animals_sorted[['name']]
    
    return result

# Ejemplo de uso
data = {
    'name': ['Elephant', 'Tiger', 'Giraffe', 'Zebra', 'Lion'],
    'species': ['Elephas', 'Panthera', 'Giraffa', 'Equus', 'Panthera'],
    'age': [10, 5, 15, 8, 7],
    'weight': [5000, 250, 800, 300, 190]
}
animals = pd.DataFrame(data)

heavy_animals = findHeavyAnimals(animals)
print(heavy_animals)
