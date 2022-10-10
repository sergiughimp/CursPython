'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
'''
def get_numere_pare(lista_nr):
    lista_noua = []
    for numar in lista_nr:
        if numar % 2 == 0:
            lista_noua.append(numar)
    return lista_noua

def get_numere_impare(lista_nr):
    lista_noua = []
    for numar in lista_nr:
        if numar % 2 != 0:
            lista_noua.append(numar)
    return lista_noua

def get_numere_pozitive(lista_nr):
    lista_noua = []
    for numar in lista_nr:
        if numar > 0:
            lista_noua.append(numar)
    return lista_noua

def get_numere_negative(lista_nr):
    lista_noua = []
    for numar in lista_nr:
        if numar < 0:
            lista_noua.append(numar)
    return lista_noua

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = get_numere_pare(alte_numere)
numere_impare = get_numere_impare(alte_numere)
numere_pozitive = get_numere_pozitive(alte_numere)
numere_negative = get_numere_negative(alte_numere)

print(f"Numerele pare sunt {numere_pare}")
print(f"Numerele pare sunt {numere_impare}")
print(f"Numerele pare sunt {numere_pozitive}")
print(f"Numerele pare sunt {numere_negative}")


'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
'''

def piramida(numar):
    for i in range(1, numar + 1):
        print(f"{i}" * i)

# numar_piramida = int(input("Introduceti numarul: \n"))
numar_piramida = 7
print(piramida(numar_piramida))

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
'''
import random

# functia ai ghicit va returna True daca s-a ghicit numarul, si False altfel. Va si afisa mesajul de "mai mic", "mai mare"
def ai_ghicit(nr_secret, nr_ghicit):
    if nr_secret == nr_ghicit:
        print(f"Felicitari! ai ghicit! numarul secret este egal cu {nr_ghicit}")
        return True
    if nr_ghicit > nr_secret:
        print(f"Numarul secret e mai mic {nr_ghicit}, mai incearca")
    else:
        print(f"Numarul secret e mai mare {nr_ghicit}, mai incearca")
    return False
numar_secret = random.randint(1, 30)  # alegem un numar aleator intre 1 si 30
incercari = 0
max_incercari = 10
while incercari < max_incercari:
    incercari += 1
    numar_ghicit = int(input("Ghiceste: \n"))
    if ai_ghicit(numar_secret, numar_ghicit):
        print(f"Ai ghicit din {incercari} incercari!")
        break
else:
    # Aici se ajunge doar daca while nu a ajuns deloc la un break
    print(f"Nu ai ghicit din {max_incercari} incercari, jocul s-a terminat. Ai pierdut")