"""Fitxer amb totes les funcions requerides per l'exercici 2"""

import pandas as pd


# 2 a)


def find_max_col(dataframe: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """Funció que retorna les files on hi ha el valor màxim d'una columna completa,
    es pot determinar quines columnes torna.
    Paràmetres:
    - dataframe: dataframe que conté les dades
    - filter_col: nom de la columna de la qual volem saber el màxim
    - cols_to_return: llista de columnes que cal retornar.
    Returns:
    Dataframe amb només les files on la columna especificada té el valor màxim,
    amb les columnes que s'especifiquen.
    """
    return dataframe.loc[dataframe[filter_col] == dataframe[filter_col].max()][cols_to_return]


# 2 b)

def find_rows_query(dataframe: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """Funció que fa de filtre avançat retornant un dataframe amb els filtres
    proporcionats a la tuple. Per exemple ([“league_name”, “weight_kg”],
    [“English Premier League”, (60, 70)]) Tornaria els jugadors i les jugadores
    de la lliga “English Premier League” amb un pes entre 60 i 70 quilos (inclosos).
    Paràmetres:
    - dataframe: dataframe que conté les dades
    - query: tupla que conté la query
    - cols_to_return: llista de columnes que cal retornar.
    Returns:
    Dataframe filtrat amb les condicions que li hem passat i amb només les columnes proporcionades.
    """

    # Detecto si el filtre és string o tuple, i aplico el .loc necessari (== o bé >= <=)
    for col, filtre in zip(query[0], query[1]):
        if isinstance(filtre, tuple):
            dataframe = dataframe.loc[(dataframe[col] >= filtre[0]) & (dataframe[col] <= filtre[1])]
        else:
            dataframe = dataframe.loc[dataframe[col] == filtre]

    return dataframe[cols_to_return]
