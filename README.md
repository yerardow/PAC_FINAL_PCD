# PAC4 - Gerard Costa Figuerola

Benvinguts a la meva PAC4 de Programació per a la ciència de dades (aula 1)

### Passos per la instal·lació:

1. Situats a la carpeta principal `pip install -r requirements.txt`
2. `python3 main.py`
3. Seguir les indicacions, anar posant el número de cada exercici
4. Escriure `exit` per sortir

### Pylint

El projecte conté el main i els exercicis a la carpeta principal i després té tots els útils a la carpeta "utils".

Per tant, per executar pylint a la totalitat dels arxius:
1. Situats a la carpeta principal: `pylint *.py`
2. `cd utils` per anar a la carpeta "utils"
3. Situats a la carpeta utils`pylint *.py`
4. `cd ..` per tornar a la carpeta principal

### Testos i HTMLTestRunner

Els testos són a la carpeta tests, tant els públics com els custom

Per defecte HTMLTestRunner no està instal·lat, per tant, abans d'executar els tests:

- Situats a la carpeta principal: `pip install HTMLTestRunner-rv`

Una vegada insta·lat, ja es poden executar els dos sets de tests:
- `python3 -m tests.test_public`
- `python3 -m tests.test_custom`