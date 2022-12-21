"""Main de l'exercici 5, on s'utilitzen la funció creada anteriorment a utils_ex5"""

import matplotlib.pyplot as plt
from utils.utils_ex1 import join_datasets_year
from utils.utils_ex4 import players_dict, clean_up_players_dict
from utils.utils_ex5 import top_average_column


if __name__ == "__main__":
    print('Buscant els històrics i generant dades, pot tardar +40 segons...')

    # Importem les dades
    DATA = join_datasets_year('data', [2016, 2017, 2018, 2019, 2020, 2021, 2022])

    # Creem el diccionari net
    COLS_INTERES = ['short_name', 'movement_sprint_speed', 'year']
    DATA_DICT = players_dict(DATA, list(DATA["sofifa_id"].unique()), COLS_INTERES)
    DATA_DICT = clean_up_players_dict(DATA_DICT, [('short_name', 'one')])

    # Creo la llista de jugadors amb més movement speed ordenada
    LLISTA_JUGADORS = top_average_column(DATA_DICT, 'short_name',
                                         'movement_sprint_speed', 7)

    # Imprimeixo els 4 primers jugadors amb més movement speed
    for i in range(4):
        print(LLISTA_JUGADORS[i])

    # Gràfic:
    X = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
    Y1 = LLISTA_JUGADORS[0][2]['value']
    Y2 = LLISTA_JUGADORS[1][2]['value']
    Y3 = LLISTA_JUGADORS[2][2]['value']
    Y4 = LLISTA_JUGADORS[3][2]['value']

    plt.plot(X, Y1, label=LLISTA_JUGADORS[0][0])
    plt.plot(X, Y2, label=LLISTA_JUGADORS[1][0])
    plt.plot(X, Y3, label=LLISTA_JUGADORS[2][0])
    plt.plot(X, Y4, label=LLISTA_JUGADORS[3][0])

    plt.title("Evolution of top 4 best movement sprint speed players", fontsize=15)
    plt.ylabel("Movement sprint speed", fontsize=13)
    plt.legend()
    plt.show()
