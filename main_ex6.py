"""Funcions per fer l'exercici 6"""

import pprint

from utils.utils_ex6 import get_top_lb_players, get_top_rb_players, \
    get_top_cb_players, try_all_teams
from utils.utils_ex1 import join_datasets_year
from utils.utils_ex2 import find_rows_query


if __name__ == "__main__":
    print('Calculant la millor defensa MASCULINA, pot tardar +30 segons...\n')

    # Defineixo les columnes per cada us (i els pesos per calcular mitjanes ponderades)
    COLS_LB_RB = ['defending', 'movement_acceleration', 'movement_sprint_speed',
                  'skill_long_passing']
    WEIGHTS_LB_RB = [2, 1, 1, 0.7]

    COLS_CB = ['defending', 'physic', 'power_strength', 'power_jumping', 'mentality_positioning']
    WEIGHTS_CB = [2, 1.5, 1, 1, 0.7]

    COLS_ATTACK = ['shooting', 'attacking_crossing', 'attacking_finishing',
                   'attacking_heading_accuracy', 'dribbling']
    COLS_DEFENSE = ['defending_marking_awareness', 'defending_standing_tackle',
                    'defending_sliding_tackle']
    COLS_CONTROL = ['skill_ball_control', 'skill_long_passing', 'passing']

    COLS_OF_INTEREST = ['short_name', 'player_positions', 'club_name', 'release_clause_eur'] + list(
        set(COLS_LB_RB + COLS_CB + COLS_ATTACK + COLS_DEFENSE + COLS_CONTROL))

    # Agafo les dades del 2022
    DATA = join_datasets_year('data', [2022])

    # CÀLCUL DE MILLOR DEFENSA MASCULINA

    DATA_MASC = find_rows_query(DATA, (['gender'], ['M']), COLS_OF_INTEREST)

    # Obtinc el top20 de jugadors a cada posició
    DATA_LB = get_top_lb_players(DATA_MASC, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_RB = get_top_rb_players(DATA_MASC, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_CB = get_top_cb_players(DATA_MASC, 20, COLS_CB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_CB)

    # Provo totes les combinacions possibles i em quedo amb la millor
    WINNER_DEFENSE = try_all_teams(DATA_LB, DATA_RB, DATA_CB)

    # Imprimeixo defensa masculina
    pprint.pprint(WINNER_DEFENSE, sort_dicts=False)

    # CÀLCUL DE MILLOR DEFENSA FEMENINA

    print('\n\nCalculant la millor defensa FEMENINA, pot tardar +30 segons...\n')
    DATA_FEM = find_rows_query(DATA, (['gender'], ['F']), COLS_OF_INTEREST)

    # Obtinc el top20 de jugadors a cada posició
    DATA_LB = get_top_lb_players(DATA_FEM, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_RB = get_top_rb_players(DATA_FEM, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_CB = get_top_cb_players(DATA_FEM, 20, COLS_CB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_CB)

    # Provo totes les combinacions possibles i em quedo amb la millor
    WINNER_DEFENSE = try_all_teams(DATA_LB, DATA_RB, DATA_CB)

    # Imprimeixo defensa femenina
    pprint.pprint(WINNER_DEFENSE, sort_dicts=False)

    # CÀLCUL DE MILLOR DEFENSA DE VETERANS/ES MIXT

    print('\n\nCalculant la millor defensa de VETERANS/ES MIXT, pot tardar +30 segons...\n')
    DATA_VET = find_rows_query(DATA, (['age'], [(30, 100)]), COLS_OF_INTEREST)

    # Obtinc el top20 de jugadors a cada posició
    DATA_LB = get_top_lb_players(DATA_VET, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_RB = get_top_rb_players(DATA_VET, 20, COLS_LB_RB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_LB_RB)
    DATA_CB = get_top_cb_players(DATA_VET, 20, COLS_CB, COLS_DEFENSE,
                                 COLS_ATTACK, COLS_CONTROL, WEIGHTS_CB)

    # Provo totes les combinacions possibles i em quedo amb la millor
    WINNER_DEFENSE = try_all_teams(DATA_LB, DATA_RB, DATA_CB)

    # Imprimeixo defensa DE VETERANS/ES MIXT
    pprint.pprint(WINNER_DEFENSE, sort_dicts=False)
