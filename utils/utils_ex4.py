"""Fitxer amb totes les funcions requerides per l'exercici 4"""

import pandas as pd
from utils.utils_ex3 import find_rows_query


# 4 a)

def players_dict(dataframe: pd.DataFrame, ids_players: list, cols: list) -> dict:
    """Funció que donat un df. unes ids de jugadors i columnes d'interès, retorna
    un diccionari aquesta informació en forma de claus i valors.
    Paràmetres:
    - df: dataframe que conté les dades
    - ids: llista d’identificador “sofifa_id”
    - cols: llista de columnes de les quals volem informació
    Returns:
    Si per exemple només volem id '192476' i columnes 'short_name' i 'year', retorna un
    diccionari en format {'192476': {'short_name': ['Fontàs', 'Fontàs', 'Fontàs'],
    'year': [2016, 2017, 2018]}}
    """

    # Inicialitzem el diccionari que contindrà tota la informació
    dict_players = {}

    # I procedim a recórrer totes les ids que ens proporcionin
    for player_id in ids_players:
        found_data = find_rows_query(dataframe, (['sofifa_id'], [player_id]), cols)
        dict_players[player_id] = found_data.to_dict('list')

    return dict_players


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """Funció que neteja el diccionari de repetits
    Paràmetres:
    - player_dict: diccionari amb el format de l’apartat (a) players_dict
    - col_query: llista de tuples amb detalls sobre la informació que cal simplificar
    per exemple ('columna', 'one') o ('columna2', 'del_rep')
    Returns:
    Un nou diccionari net
    """

    for player in list(player_dict.keys()):
        for query in col_query:

            # Si només volem un valor, el traiem de la llista i l'assignem amb la clau
            if query[1] == 'one':
                player_dict[player][query[0]] = player_dict[player][query[0]].pop()

            # Si volem treure els valors repetits, amb list(set()) es treuen
            else:  # 'del_rep'
                # Però si és player_positions, ls posicions s'han de descomposar abans
                if query[0] == 'player_positions':  # Descomponem
                    descomp_positions = []
                    for item in player_dict[player][query[0]]:
                        descomp_positions.extend(item.split(', '))
                    player_dict[player][query[0]] = list(set(descomp_positions))
                else:
                    player_dict[player][query[0]] = list(set(player_dict[player][query[0]]))

    return player_dict
