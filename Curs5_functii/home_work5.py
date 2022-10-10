'''
1.Funcție care să calculeze și să returneze suma a două numere
'''
print("Ex 1")
def suma_numere(numar1, numar2):
    return numar1 + numar2
print(f"Suma numere: {suma_numere(4, 5)}")

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
print("Ex 2")
def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
numar = 4
print(f"Paritate numarului {numar}: {este_par(numar)}")

'''
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
print("Ex 3")
def calculeaza_lungime_nume(nume, prenume, nume_mijlociu=""):
    return len(nume) + len(prenume) + len(nume_mijlociu)
print(f"Numarul total de caractere din numele complet este: {calculeaza_lungime_nume('Ghimp', 'Sergiu')}" )
print(f"Numarul total de caractere din numele complet este: {calculeaza_lungime_nume('Briceag', 'Marcela', 'Elena')}" )

'''
4. Funcție care returnează aria dreptunghiului
'''
print("Ex 4")
def aria_dreptunghiului(lungime, latime):
    return lungime * latime
print(f"Aria dreptunghiului este: {aria_dreptunghiului(lungime=5, latime=3)}")

'''
5. Funcție care returnează aria cercului
'''
print("Ex 5")
import math
def aria_cercului(pi, r):
    return pi * r**2
print(f"Aria cercului este: {aria_cercului(math.pi, 7)}")

'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
'''
print("Ex 6")
def cautare_x_in_string(string, caracter):
    if caracter in string:
        return True
    else:
        return False

def is_in_string(my_char, my_str):
    for c in my_str:
        if c == my_char:
            return True # iesim din functie daca gasim caracterul cautat, nu are rost sa mai cautam
    return False # daca am ajuns aici, inseamna ca nu am gasit deloc caracterul cautat
'''
Variabilele definite in afara oricarei functii se numesc GLOBALE astfel, avem acces la ele si in interiorul functiei
Variabilele de care avem nevoie in functie ar trebui  MEREU sa fie transmise prin parametri
'''
print(f"Cautare x in string: {cautare_x_in_string('asdasxsaxqafef','z')}")
print(is_in_string('s', "dadasdas"))


'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
print("Ex 7")
def is_lower_upper_counter(string):
    cnt_upper = 0
    cnt_lower = 0
    for i in string:
        if i.upper() == i:
            cnt_upper += 1
        if i.lower() == i:
            cnt_lower += 1
    print(f"Numarul de caractere uppercase este {cnt_upper}")
    print(f"Numarul de caractere lowercase este {cnt_lower}")
is_lower_upper_counter("sdaaSSS")

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
print("Ex 8")
def return_lista_numere_pozitive(list):
    positive_list = []
    for item in list:
        if item > 0:
            positive_list.append(item)
    return positive_list
list = [1, -8, 6, -7, 6, 6, -3]
print(f"Lista de numere este {list}")
print(f"Lista de numere pozitive este: {return_lista_numere_pozitive(list)}")

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
'''
print("Ex 9")
def comparare_numere(x, y):
    if x > y:
        print(f"Numarul x = {x} este mai mare decat numarul y = {y}")
    elif x < y:
        print(f"Numarul y = {y} este mai mare decat numarul x = {x}")
    else:
        print(f"Numarul x = {x} este egal cu numarul y = {y}")
comparare_numere(10, 2)

'''
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
print("Ex 10")
def adaugare_nr_set(numar, set_numare):
    if numar not in set_numare:
        set_numare.add(numar)
        print(f"Adaugam numarul {numar} in set")
        return True
    else:
        print(f"Nu adaugam numarul {numar} in set. Aceste exista deja")
        return False
set_numere = {4, 7, 2, 7, 2}
print(set_numere)
print(adaugare_nr_set(3, set_numere))

'''
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''
print("Exercitii Optionale")
print("Ex 1")
from calendar import monthrange
def number_of_days_in_month(year, month):
    return monthrange(year, month)[1]
month = 5
year = 2003
print(f"Numarul de zile din anul {year} si luna {month} este: {number_of_days_in_month(year, month)}")

'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)
● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)
'''
print("Ex 2")
# Atunci cand returnam mai multe valori dintr-o functie, acestea sunt puse automat intr-un tuple
def calculator(numar1, numar2):
    return numar1 + numar2, numar1 - numar2, numar1 * numar2, numar1 / numar2
a, b = 4, 5

s, d, p, c = calculator(a, b)
print(f"Rezultatele numerelor {a} si {b} este: Suma {s}, Diferenta {d}, Produs {p}, Cat {c}")

'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
print("Ex 3")
from pprint import pprint
def aparitie_cifra(list):

    d = dict()
    for x in range(10):
        d[x] = list.count(x)
    return d

lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
pprint(aparitie_cifra(lista))

'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''
print("Ex 4")
def numar_maxim(numar1, numar2, numar3):
    if numar1 > numar2 and numar1 > numar2:
        return numar1
    elif numar2 > numar1 and numar2 > numar3:
        return numar2
    else:
        return numar3
a, b, c = 2, 4, 1
print(f"Numarul maxim este: {numar_maxim(a, b, c)}")
'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
print("Ex 5")
def suma_numerelor(numar):
    suma = 0
    for i in range(0, numar+1):
        suma += i
    return suma
print(f"Suma tuturor numerelor de la 0 la acel numar este: {suma_numerelor(3)}")

'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''
print("Exercitii Optionale - Bonus")
print("Ex 1")
def numere_comune_lista(list1, list2):
    return [value for value in list1 if value in list2]
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(numere_comune_lista(list1, list2))

'''
2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''
print("Ex 2")
def reducere_produs(pret, procent_reducere):
    if 0 < procent_reducere < 100:
        print("Reducerea se aplica")
        pret -= (procent_reducere * pret) / 100
    else:
        print("Reducerea nu se aplica")
    return pret
print(f"Pretul final al produsului este {reducere_produs(100, 99)}")

'''
3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''
print("Ex 3")
from datetime import datetime
import pytz

def current_time(city):
    if city == "New York":
        tz_NY = pytz.timezone('America/New_York')
        datetime_NY = datetime.now(tz_NY)
        print("NY time:", datetime_NY.strftime("%H:%M:%S"))
    elif city == "London":
        tz_London = pytz.timezone('Europe/London')
        datetime_London = datetime.now(tz_London)
        print("London time:", datetime_London.strftime("%H:%M:%S"))
    elif city == "Bucharest":
        tz_Bucharest = pytz.timezone('Europe/Bucharest')
        datetime_Bucharest = datetime.now(tz_Bucharest)
        print("Bucharest time:", datetime_Bucharest.strftime("%H:%M:%S"))
current_time("Bucharest")