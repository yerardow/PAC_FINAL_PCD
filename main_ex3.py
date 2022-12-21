"""Main de l'exercici 3, on s'utilitzen les funcions creades a l'exercici 1 i 2 i es mostren
els resultats per pantalla."""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from utils.utils_ex1 import join_datasets_year
from utils.utils_ex3 import calculate_bmi

if __name__ == "__main__":
    # a)

    # Importem les dades
    DATAFRAME = join_datasets_year('data', [2022])

    # Filtrem 'M' i 2022 i calculem BMI
    DATAFRAME = calculate_bmi(DATAFRAME, 'M', 2022, ['club_flag_url'])

    # Creem una nova columna de 'pais' tallant les webs de la columna 'club_flag_url'
    DATAFRAME['pais'] = DATAFRAME.club_flag_url.str.split('.').str[2].str.split('/').str[2]

    # Agrupem per país i calculem la mitjana del BMI
    GROUPED_BY_COUNTRY = DATAFRAME[['pais', 'BMI']].groupby('pais').max()

    # Creem el gràfic
    BARS = list(GROUPED_BY_COUNTRY.index)
    Y_POS = np.arange(len(BARS))
    BMI = list(GROUPED_BY_COUNTRY.BMI)
    plt.figure(figsize=(15, 12))

    plt.bar(Y_POS, BMI)

    plt.xticks(Y_POS, BARS)
    plt.xticks(rotation=45)

    # Podem veure que en quasi tots els països el BMI màxim dels jugadors està dins de la
    # categoria "overweight", cosa que si ens fixessim estrictament en aquesta mètrica
    # arribarem a la conclusió que molts tenen sobrepès.

    print('Podem veure que en quasi tots els països el BMI màxim dels jugadors està dins de la '
          'categoria "overweight", cosa que si ens fixessim estrictament en aquesta mètrica '
          'arribarem a la conclusió que molts tenen sobrepès.')

    # b)

    # Agafo dades dels homes espanyols entre 18 i 34, el més semblant a l'edat dels futbolistes
    BMI_SPAIN = pd.read_csv('data/bmi_spain.csv', sep=';')
    BMI_SPAIN = BMI_SPAIN.replace(',', '', regex=True)
    BMI_SPAIN = BMI_SPAIN.astype({"Total": float}, errors='raise')
    SPAIN_GROUPED_CAT_BMI = BMI_SPAIN[['Adult body mass index', 'Total']] \
        .groupby('Adult body mass index').sum()
    TOTAL_MEN = SPAIN_GROUPED_CAT_BMI.Total.sum()
    SPAIN_GROUPED_CAT_BMI['percent'] = (SPAIN_GROUPED_CAT_BMI.Total / TOTAL_MEN) * 100


    # Creem nova columna amb les categories amb el df de jugadors homes
    def categoritzar(fila):
        """Categoritza la variable BMI"""
        bmi = fila.BMI
        if bmi < 18.5:
            return "Underweight (BMI < 18.5 kg/m2)"
        if 18.5 <= bmi < 25:
            return "Normal weight (18.5 kg/m2 <= BMI < 25 kg/m2)"
        if 25 <= bmi < 30:
            return "Overweight (25 kg/m2 <= BMI < 30 kg/m2)"
        return "Obesity (BMI >= 30 kg/m2)"


    # Apliquem la categorització a cada fila
    DATAFRAME["Adult body mass index"] = DATAFRAME.apply(categoritzar, axis=1)
    DATAFRAME['count'] = ""

    # Agrupem per categoria i comptem
    PLAYERS_GROUPED_CAT_BMI = DATAFRAME[["Adult body mass index", "count"]] \
        .groupby("Adult body mass index").count()
    TOTAL_PLAYERS = PLAYERS_GROUPED_CAT_BMI['count'].sum()
    PLAYERS_GROUPED_CAT_BMI['percent'] = (PLAYERS_GROUPED_CAT_BMI['count'] / TOTAL_PLAYERS) * 100

    # Fem segon gràfic:
    CATEGORIES = ['Normal weight', 'Obesity', 'Overweight', 'Underweight']
    BMI_PLAYERS = list(PLAYERS_GROUPED_CAT_BMI.percent)
    BMI_SPAIN = list(SPAIN_GROUPED_CAT_BMI.percent)

    plt.figure(figsize=(8, 13))
    X_AXIS = np.arange(len(CATEGORIES))

    plt.bar(X_AXIS - 0.2, BMI_SPAIN, 0.4, label="% d'homes [18-34] anys")
    plt.bar(X_AXIS + 0.2, BMI_PLAYERS, 0.4, label="% d'homes jugadors de futbol")

    plt.xticks(X_AXIS, CATEGORIES)
    plt.ylabel("Vegades")
    plt.xticks(rotation=60)
    plt.legend()

    plt.show()

    print('\n\nAl segon gràfic veiem que la gran majoria de futbolistes tenen un BMI normal '
          'i una part petita tenen sobrepès. En canvi, a la població general d\'homes '
          'd\'entre 18 i 34 anys (edat aprox dels futbolistes) hi ha molt més percentatge '
          'de sobrepès i inclús d\'obesitat')
