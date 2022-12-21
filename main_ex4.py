"""Main de l'exercici 4, on s'utilitzen les funcions creades als apartats a) i b)"""

import pprint
from utils.utils_ex1 import join_datasets_year
from utils.utils_ex4 import players_dict, clean_up_players_dict


if __name__ == "__main__":
    # Importo les dades dels anys corresponents
    DATA = join_datasets_year('data', [2016, 2017, 2018])

    print('\nDiccionari brut:\n')

    # Creo el diccionari en brut
    DICT_BRUT = players_dict(DATA, [226328, 192476, 230566],
                             ["short_name", "overall", "potential", "player_positions", "year"])

    # Imprimeixo el diccionari en brut
    pprint.pprint(DICT_BRUT)

    print("\nQuery per netejar el diccionari: [('player_positions', 'del_rep'), "
          "('short_name', 'one')]")

    print('\nDiccionari net:\n')

    # Creo el diccionari en net
    DICT_NET = clean_up_players_dict(DICT_BRUT, [('player_positions', 'del_rep'),
                                                 ('short_name', 'one')])

    # Imprimeixo el diccionari en net
    pprint.pprint(DICT_NET)
