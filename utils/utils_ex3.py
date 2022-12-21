"""Fitxer amb totes les funcions requerides per l'exercici 3"""

import copy
import pandas as pd
from utils.utils_ex2 import find_rows_query


# 3


def calculate_bmi(dataframe: pd.DataFrame, gender: str, year: int,
                  cols_to_return: list) -> pd.DataFrame:
    """Funció que calcula el BMI dels jugadors amb gènere i any proporcionats i retorna un df amb
    les columnes demanades i una última amb el BMI.
    Paràmetres:
    - df: dataframe que conté les dades
    - gender: gènere que volem estudiar
    - year: any que volem estudiar en format XXXX (per exemple 2020)
    - cols_to_return: llista de columnes que cal retornar (sense columna BMI)
    Returns:
    Un dataframe amb les columnes proporcionades + una altra amb el BMI calculat
    """

    cols_plus_weight_height = copy.copy(cols_to_return)
    cols_plus_weight_height.extend(['height_cm', 'weight_kg'])

    filtered_df = find_rows_query(dataframe, (['gender', 'year'], [gender, year]),
                                  cols_plus_weight_height)
    filtered_df['BMI'] = filtered_df['weight_kg'] / pow((filtered_df['height_cm'] / 100), 2)

    cols_to_return.append('BMI')
    return filtered_df[cols_to_return]
