"""Main de l'exercici 2, on s'utilitzen les funcions creades a l'exercici 1 i 2 i es mostren
els resultats per pantalla."""

from utils.utils_ex1 import join_datasets_year
from utils.utils_ex2 import find_max_col, find_rows_query


if __name__ == "__main__":
    # Primer agafem les dades del 2016 al 2022
    DATA = join_datasets_year('data', [2016, 2017, 2018, 2019, 2020, 2021, 2022])

    # Apliquem el filtre avançat
    FILTERED_DF = find_rows_query(DATA, (['gender', 'nationality_name', 'age'],
                                         ['M', 'Belgium', (0, 24)]),
                                  ['short_name', 'year', 'age', 'overall', 'potential'])

    # Busquem només els que tenen màxim potencial, partint
    # dels resultats del filtre avançat
    MAX_POTENTIAL = find_max_col(FILTERED_DF, 'potential', ['short_name', 'year', 'age', 'overall',
                                                            'potential'])

    # Imprimim resultats per pantalla
    print('\nJugadors de nacionalitat belga menors de 25 anys màxim “potential” '
          'al futbol masculí:\n')
    print(MAX_POTENTIAL)

    # La segona part, filtrem amb el filtre avançat
    FILTERED_DF2 = find_rows_query(DATA, (['gender', 'player_positions', 'age', 'potential'],
                                          ['F', 'GK', (29, 100), (86, 100)]),
                                   ['short_name', 'year', 'age', 'overall', 'potential'])
    # I imprimim per pantalla
    print('\n\nPorteres majors de 28 anys amb “overall” superior a 85 al futbol femení:\n')
    print(FILTERED_DF2)
