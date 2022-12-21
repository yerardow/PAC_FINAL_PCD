"""Funcions per fer l'exercici 6"""

import numpy as np
import pandas as pd


def get_top_lb_players(data: pd.DataFrame, top: int, cols_rb_lb: list, cols_defense: list,
                       cols_attack: list, cols_control: list, weights: list) -> pd.DataFrame:
    """Funció que calcula una puntuació per cada lateral esquerra i
    obté el top a partir d'un dataset de jugadors/es. També calcula puntuacions de
    contribució en defensa, atac i possessió per utilitzar en fer els equips.
    Paràmetres:
    - data: Dataset amb estadístiques de molts jugadors
    - top: Fins a quin top es vol arribar, ex: top=10 només retorna els millors 10
    Returns:
    Un nou dataset amb el top n de millors laterals esquerres amb el nom, l'equip, la
    clàusula de rescissió i les mitjanes calculades.
    """

    # Obtenim només els laterals esquerres
    data_lb = data.loc[data['player_positions'].str.contains("LB")].reset_index()

    # Calculem les mitjanes corresponents
    data_lb['mean_lb'] = np.average(data_lb[cols_rb_lb], weights=weights, axis=1)
    data_lb['mean_defense'] = data_lb[['mean_lb'] + cols_defense].mean(axis=1)
    data_lb['mean_attack'] = data_lb[cols_attack].mean(axis=1)
    data_lb['mean_control'] = data_lb[cols_control].mean(axis=1)

    # Ordenem per la puntuació com a lateral esquerre (mean_lb)
    data_lb = data_lb.sort_values('mean_lb', ascending=False)

    # Retornem les n primeres posicions
    return data_lb.head(top).reset_index()[['short_name', 'club_name', 'release_clause_eur',
                                            'mean_lb', 'mean_defense',
                                            'mean_attack', 'mean_control']]


def get_top_rb_players(data: pd.DataFrame, top: int, cols_rb_lb: list, cols_defense: list,
                       cols_attack: list, cols_control: list, weights: list) -> pd.DataFrame:
    """Funció que calcula una puntuació per cada lateral dret i
    obté el top a partir d'un dataset de jugadors/es. També calcula puntuacions de
    contribució en defensa, atac i possessió per utilitzar en fer els equips.
    Paràmetres:
    - data: Dataset amb estadístiques de molts jugadors
    - top: Fins a quin top es vol arribar, ex: top=10 només retorna els millors 10
    Returns:
    Un nou dataset amb el top n de millors laterals drets amb el nom, l'equip, la
    clàusula de rescissió i les mitjanes calculades.
    """

    # Obtenim les dades només de laterals drets
    data_rb = data.loc[data['player_positions'].str.contains("RB")].reset_index()

    # Calculem les mitjanes corresponents
    data_rb['mean_rb'] = np.average(data_rb[cols_rb_lb], weights=weights, axis=1)
    data_rb['mean_defense'] = data_rb[['mean_rb'] + cols_defense].mean(axis=1)
    data_rb['mean_attack'] = data_rb[cols_attack].mean(axis=1)
    data_rb['mean_control'] = data_rb[cols_control].mean(axis=1)

    # Ordenem per la puntuació com a lateral dret
    data_rb = data_rb.sort_values('mean_rb', ascending=False)

    # Retornem les n primeres posicions
    return data_rb.head(top).reset_index()[['short_name', 'club_name', 'release_clause_eur',
                                            'mean_rb', 'mean_defense',
                                            'mean_attack', 'mean_control']]


def get_top_cb_players(data: pd.DataFrame, top: int, cols_cb: list, cols_defense: list,
                       cols_attack: list, cols_control: list, weights: list) -> pd.DataFrame:
    """Funció que calcula una puntuació per cada central i
    obté el top a partir d'un dataset de jugadors/es. També calcula puntuacions de
    contribució en defensa, atac i possessió per utilitzar en fer els equips.
    Paràmetres:
    - data: Dataset amb estadístiques de molts jugadors
    - top: Fins a quin top es vol arribar, ex: top=10 només retorna els millors 10
    Returns:
    Un nou dataset amb el top n de millors centrals amb el nom, l'equip, la
    clàusula de rescissió i les mitjanes calculades.
    """

    # Obtenim les dades només de centrals
    data_cb = data.loc[data['player_positions'].str.contains("CB")].reset_index()

    # Calculem les mitjanes corresponents
    data_cb['mean_cb'] = np.average(data_cb[cols_cb], weights=weights, axis=1)
    data_cb['mean_defense'] = data_cb[['mean_cb'] + cols_defense].mean(axis=1)
    data_cb['mean_attack'] = data_cb[cols_attack].mean(axis=1)
    data_cb['mean_control'] = data_cb[cols_control].mean(axis=1)

    # Ordenem per la puntuació com a central
    data_cb = data_cb.sort_values('mean_cb', ascending=False)

    # Retornem les n primeres positions
    return data_cb.head(top).reset_index()[['short_name', 'club_name', 'release_clause_eur',
                                            'mean_cb', 'mean_defense',
                                            'mean_attack', 'mean_control']]


def calculate_team_scores(lb_player, rb_player, cb_player1, cb_player2) -> list:
    """Funció que calcula les puntuacions defensa, atac i possessió per cada equip de defensa
    Paràmetres:
    - lb_player: lateral esquerra
    - rb_player: lateral dret
    - cb_player1: central 1
    - cb_player2: central 2
    Returns:
    Una llista amb la puntuació total, la de defensa, la d'atac i la de possessió.
    """

    total_defense_mean = (lb_player['mean_defense'] + rb_player['mean_defense']
                          + cb_player1['mean_defense'] + cb_player2['mean_defense']) / 4

    total_attack_mean = (lb_player['mean_attack'] + rb_player['mean_attack']
                         + cb_player1['mean_attack'] + cb_player2['mean_attack']) / 4

    total_control_mean = (lb_player['mean_control'] + rb_player['mean_control']
                          + cb_player1['mean_control'] + cb_player2['mean_control']) / 4

    total_score = (total_defense_mean + total_attack_mean + total_control_mean) / 3

    return [total_score, total_defense_mean, total_attack_mean, total_control_mean]


def update_winner_defense(score: list, lb_player, rb_player, cb_player1, cb_player2) -> dict:
    """Funció que actualitza el diccionari amb la millor defensa
    Paràmetres:
    - score: llista amb les puntuacions de l'equip (defensa)
     - lb_player: lateral esquerra
    - rb_player: lateral dret
    - cb_player1: central 1
    - cb_player2: central 2
    Returns:
    Un diccionari amb les estadístiques de l'equip i nom i informació dels seus components.
    """

    return {'team_score': score[0],
            'partial_scores':
                {'defense': score[1],
                 'attack': score[2],
                 'control': score[3]},
            'team': [
                {'name': lb_player['short_name'], 'position': 'LB',
                 'current_team': lb_player['club_name'],
                 'release_clause_eur': lb_player['release_clause_eur']},
                {'name': rb_player['short_name'], 'position': 'RB',
                 'current_team': rb_player['club_name'],
                 'release_clause_eur': rb_player['release_clause_eur']},
                {'name': cb_player1['short_name'], 'position': 'CB',
                 'current_team': cb_player1['club_name'],
                 'release_clause_eur': cb_player1['release_clause_eur']},
                {'name': cb_player2['short_name'], 'position': 'CB',
                 'current_team': cb_player2['club_name'],
                 'release_clause_eur': cb_player2['release_clause_eur']}]}


def try_all_teams(data_lb: pd.DataFrame, data_rb: pd.DataFrame, data_cb: pd.DataFrame) -> dict:
    """Funció que prova totes les combinacions possibles de defenses i es queda amb la millor
    Paràmetres:
    - data_lb: Dataframe amb els millors laterals esquerres
    - data_rb: Dataframe amb els millors laterals drets
    - data_cb: Dataframe amb els millors centrals
    Returns:
    Un diccionari amb el millor equip de defensa (amb un LB, dos CB i un RB)
    """

    winner_defense = {'team_score': 0}

    for i, lb_player in data_lb.iterrows():
        for j, rb_player in data_rb.iterrows():
            for k, cb_player1 in data_cb.iterrows():
                for p, cb_player2 in data_cb.iterrows():

                    list_players = [lb_player['short_name'], rb_player['short_name'],
                                    cb_player1['short_name'], cb_player2['short_name']]

                    if len(list_players) == np.unique(list_players).size:
                        score = calculate_team_scores(lb_player, rb_player, cb_player1, cb_player2)

                        if score[0] > winner_defense['team_score']:
                            winner_defense = update_winner_defense(score, lb_player,
                                                                   rb_player, cb_player1,
                                                                   cb_player2)
    return winner_defense
