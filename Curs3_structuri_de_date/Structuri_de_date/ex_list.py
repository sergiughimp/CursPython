'''
Listele - structuri de date (colectii in python) care pot tine mai multe valori
Valorile se pot accesa prin indice (pozitia valorii din lista)
'''
list1 = [5, 7, 12, -3, 8]
list2 = ["Ana", "are", "mere"]
list3 = [True, False, True, False, False, True]

#         0        1       2       3          4         5
tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]

print(f"in vagonul 1 avem {tren[1]}")
print(tren[1:4]) # slicing functioneaza pe liste exact ca si la stringuri
print(f"in ultimul vagon avem {tren[-1]}") # indexare negativa
print(f"trenul are in total {len(tren)} vagoane") # lungimea listei se determina cu functia len

# pentru a adauga elemente noi in lista, folosim o functie numita append
print(tren)
tren.append("ovaz")
print(tren, len(tren))

# listele nu trebuie obligatoriu sa aibe elemente cu acelasi tip
lista_complexa = ['string', True, 12, 'alt string', 3.14, 'alt string']
print(lista_complexa)

lista_complexa.remove("alt string") # sterge un element din lista bazat pe valoare
print(lista_complexa)
var_pop = lista_complexa.pop(1)
print(f"Am scos din lista, de la indicile 1, valoare {var_pop}")
print(lista_complexa)

lista_complexa.clear() #sterge toate elemntele din lista
print(lista_complexa)

del lista_complexa # sterge variabila lista_complexa
#     0    1    2    3    4    5    6    7
l = ['a', 'b', 'c', 'a', 'b', 'x', 'z', 'b']
index_1b = l.index("b") # returneaza indexul la care gasim valoare din paranteze
print(index_1b)
# ca sa gasim al doilea b, trebuie sa facem slicing si sa incepem cautarea de la pozitia primului  + 1
# deoarece prin slicing avem o noua lista, mai scurta, vom obtine un idex mai mic decat cel real. Pentru a rezolva problema asta, trebuie sa tinem cont ca sunt 'index_1b + 1' elemente pe care nu le luam in considerare
print(f"Cautam acum cu slicing in sub-lista{l[index_1b + 1:]}")
#   0    1    2    3    4    5
# ['c', 'a', 'b', 'x', 'z', 'b']

#  in sub-lista, al doilea b va fi in pozitia 2, dar sub-lista noastra, comparat cu lista originala, este mai scurta cu 2 elemente. ceea ce inseamna ca in lista originala al doilea b se gasste la pozitia 4
index_2b = l[index_1b + 1:].index("b") + index_1b + 1
print(index_2b)
index_3b = l[index_2b + 1:].index("b") + index_2b + 1
print(index_3b)

# deoarece putem sa adaugam/stergem/modificam elemente din lista, zicem ca lista e Mutabila
l[0] = l[0].upper()
l[1] = l[1].upper()

print(l)

# Functii pe liste: max, min, sum
lx = [5, 7, 12, -3, 8, 2, 3, 21]
print(max(lx))
print(min(lx))
print(sum(lx))

# list membership: verificare daca o valoare se gaseste intr-o lista
print(7 in lx) # True
print(6 in lx) # False

vocale = ['a', 'e', 'i', 'o', 'u']
# litera = input("Litera: \n")
litera = 'a'

if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print("Litera este vocala")

if litera in vocale:
    print("Litera este vocala")

# Concatenarea (adunarea) a doua liste
ly = [70, 33, 14, 51]
lz = lx + ly
print(f"Lx: {lx} \nLy: {ly}")
print(lz)

# a doua modalitate este cu metoda extend (se va modifica lista pe care facem extend)
lx.extend(ly)
print(f"Lx este acum {lx}")