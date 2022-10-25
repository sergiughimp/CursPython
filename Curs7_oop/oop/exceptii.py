'''

Exceptii: clase speciale Python folosite atunci cand ceva nu merge bine in cod

Folosim mecanismul try-except pentru a gestiona posibilele exceptii aparute in codul nostrum astfel incat programul sa NU se opreasca

try:
    incearca ceva aici care s-ar putea sa dea exceptie
except NumeExceptie as e:
    aici gestionam exceptia cum consideram noi
'''

l = [1, 2, 3, 4]
print(l[0])
try:
    print(l[5])
except IndexError as e:
    print("Am dat de o eroare de tipul IndexError")
    print(e)
print(l[3])
'''
Unde am putea folosi try-except:
    - input de la utilizator (verifica daca am primit ce asteptam noi)
'''
try:
    varsta = int(input("Introduceti varsta: \n"))
    print(f"Ati introdus {varsta}")
except ValueError as e:
    print("Nu ati introdus un numar")


'''
Reguli pentru prinderea exceptiilor:
    - avem mereu un singur try, dar putem aveam mai multe except
    - daca avem mai multe exceptii posibile, trebuie sa punem de la cea mai specifica, la cea mai generica
    - la final, putem avea inclusiv un except "gol", care sa prinda orice alta exceptie la care nu ne-am gandit noi
'''

try:
    nr_par = int(input("Introduceti un numar par: \n"))
    assert nr_par % 2 == 0
except ValueError as e: # -> daca facem 'as e', ii dam un nume de variabila exceptiei, si o putem folosi intr-un blocui ei
    print("Nu ati introdus un numar")
except AssertionError as e:
    print("Numarul nu este par")
except:
    # in general nu se face asa, sa nu specificam exceptia pe care o prindem
    print("a aparut alta exceptie, nu stim care...")
print("Am terminat")
