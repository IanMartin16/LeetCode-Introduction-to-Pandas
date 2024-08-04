import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Devuelve el número de filas y columnas del DataFrame
    return [players.shape[0], players.shape[1]]

# Definición del DataFrame players con datos de ejemplo
data = {
    'player_id': [1, 2, 3, 4],
    'name': ['Player1', 'Player2', 'Player3', 'Player4'],
    'age': [22, 25, 24, 23],
    'position': ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']
}

players = pd.DataFrame(data)

# Llamada a la función getDataframeSize
result = getDataframeSize(players)

# Muestra el resultado
print(result)
