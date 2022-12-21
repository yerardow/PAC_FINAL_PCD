"""Fitxer amb totes les funcions requerides per l'exercici 1"""
import os
import pandas as pd


# 1 a)


def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """Llegeix un df i afegeix dues columnes noves, una amb el gènere i l'altre amb l'any
    Paràmetres:
    - filepath: string amb la ruta de l’arxiu que volem llegir
    - gender: 'M' o 'F' (segons les sigles de “Male” or “Female”)
    - year: Any al qual corresponen les dades en format XXXX (per exemple, 2020)
    Returns:
    Dataframe amb les dues columnes noves"""

    dataframe_to_add_cols = pd.read_csv(filepath, low_memory=False)
    dataframe_to_add_cols['gender'] = gender
    dataframe_to_add_cols['year'] = year

    return dataframe_to_add_cols


# 1 b)


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """Ajunta els dos dataframes (masculí i femení) de l'any proporcionat i ho retorna
    Paràmetres:
    - path: ruta a la carpeta que conté les dades
    - year: any del que es volen llegir les dades, format XXXX (per exemple, 2020)
    Returns:
    El nou df amb masculí i femení ajuntat, amb les dues noves columnes de gènere i any
    """

    filepath_masc = os.path.join(path, "players_" + str(year - 2000) + '.csv')
    filepath_fem = os.path.join(path, "female_players_" + str(year - 2000) + '.csv')
    df_masc = read_add_year_gender(filepath_masc, 'M', year)
    df_fem = read_add_year_gender(filepath_fem, 'F', year)

    return pd.concat([df_masc, df_fem])


# 1 c)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """Funció que ajunta tots els datasets d'homes i dones d'uns anys concrets i el retorna
    Paràmetres:
    - path: ruta a la carpeta que conté les dades
    - years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]
    Returns:
    Un df amb homes i dones de cada any de la llista passada com a paràmetre
    """

    list_path = [path for _ in range(len(years))]
    return pd.concat(map(join_male_female, list_path, years))
