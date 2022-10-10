'''
Recapitulare:
1. Variabile = zona de memorie din calculator unde se pastreaza date
2. Tipuri de date: char, string, int, double/float, boolean
'''

''' Operatori:
    1. aritmetici: +, -, *, /, %
    2. de comparare: <, >, ==, !=, >=, <=
    3. logici: &&, ||
    
    Flow Control: 
    1. if
    2. if ... 
        else
    3. if...
        else ...
        if ...
'''

# operatori aritmetici
a = 6
b = 5
a = b # suprascriere
print(f'Operator "adunare": {a + b}')
print(f'Operator "scadere": {a - b}')
print(f'Operator "impartire": {a / b}')
print(f'Operator "inmultiere": {a * b}')
print(f'Operator "modulo": {a % b}')

# operatori de comparare
print(f'Operaror "mai mare": {12 > a}')
print(f'Operaror "mai mic": {12 < a}')
print(f'Operaror "egal": {12 == a}')
print(f'Operaror "diferit": {12 != a}')
print(f'Operaror "mai mare_egal": {12 >= a}')
print(f'Operaror "mai mic_egal": {12 <= a}')
# operatori logici
print(f'Operator "and": {7 > b and 8 > b}') # True and True -> True
print(f'Operator "not": {not (7 > b and 8 > b)}') # False (True and True) -> False
print(f'Operator "or": {12 > 3 or 12 < 3}') # True or False -> True