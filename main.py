"""Main de la PAC4, un programa que agafa ordres de la terminal i executa l'exercici corresponent"""

import os


INPUT_TERMINAL = True

while INPUT_TERMINAL:
    print("\nIntrodueix nombre d'exercici per executar, del 2 al 6, o bé exit per sortir")
    EXERCICI = input()

    if EXERCICI == 'exit':
        INPUT_TERMINAL = False
    elif EXERCICI == '2':
        os.system('python3 main_ex2.py')
    elif EXERCICI == '3':
        os.system('python3 main_ex3.py')
    elif EXERCICI == '4':
        os.system('python3 main_ex4.py')
    elif EXERCICI == '5':
        os.system('python3 main_ex5.py')
    elif EXERCICI == '6':
        os.system('python3 main_ex6.py')
    else:
        print('No vàlid, introdueix nombre entre 2 i 6 o exit per sortir\n')
