"""Fitxer amb totes les funcions requerides per l'exercici 5"""

import numpy as np


def average(lst):
    """Funció auxiliar que retorna la mitjana d'una llista"""
    return sum(lst) / len(lst)


def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """Funció que retorna una tupla ordenada per la columna que s'indiqui amb la mitjana
    i altres valors.
    Paràmetres:
    - data: diccionari “net” que conté la informació de diversos sofifa_id
    - identifier: columna/clau que es fara servir com identificador
    - col: nom d’una columna/clau numérica
    - threshold: mínim número de dades necessàries (anys) per no descartar
    el jugador (si hi ha NaN tmb)
    Returns:
    LLista de tuples (una per jugador) per exemple si identifier = 'short_name', col = 'shooting'
    i threshold = 2, un dels jugadors (tuples) de l'output seria:
    ('Fontàs', 48.0, {'value': [48.0, 48.0, 48.0], 'year': [2016, 2017, 2018]})
    """

    # Definim la llista de tuples que haurem d'omplir
    llista_tuples = []

    # Comencem el bucle per omplir-la
    for jugador in list(data.keys()):
        # Si hi ha les dades necessaries i no hi ha nan
        if (len(data[jugador][col]) >= threshold) & (not np.all(np.isnan(data[jugador][col]))):
            # Calculem mitjana de la columna que ens interessa
            mean_col = average(data[jugador][col])
            # Creem la tupla del jugador
            tupla = data[jugador][identifier], mean_col, \
                    {'value': data[jugador][col], 'year': data[jugador]['year']}
            # Afegim la tupla creada a la llista de tuples que haurem de retornar
            llista_tuples.append(tupla)

    return sorted(llista_tuples, key=lambda player: player[1], reverse=True)
