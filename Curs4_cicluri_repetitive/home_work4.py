import random

'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
print("Ex 1")
masini = ['Audi', 'BMW', 'Mercedes', 'Aston Martin', 'Lastrun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(masini)):
    print(f"Masina mea preferata este {masini[i]}")

print("*" * 110)

for masina in masini:
    print(f"Masina mea preferata este {masina}")

print("*" * 110)

i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i += 1
print("*" * 110)

'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
print("Ex 2")
for i in range(0, len(masini)):
    if i == 0 or i == len(masini)-1:
        continue
    masini[i] = masini[i].upper()
print(masini)
print("*" * 110)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
'''
print("Ex 3")
for masina in masini:
    if masina.lower() == "mercedes":
        print(f"Am gasit masina dorita de dvs")
        break
    else:
        print(f"Am gasit masina {masina} mai cautam")

print("*" * 110)

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
'''
print("Ex 4")
masini = ['Audi', 'BMW', 'Mercedes', 'Aston Martin', 'Lastrun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina in ['Trabant', 'Lastrun']:
        continue
    print(f"S-ar putea sa va placa masina {masina}")

print("*" * 110)

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
'''
print("Ex 5")
masini_vechi = []
for i in range(len(masini)):
    if masini[i].lower() == 'trabant' or masini[i].lower() == 'lastrun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'

print(f"Modelele vechi sunt {masini_vechi}")
print(f"Modelele noi sunt {masini}")

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
print("Ex 6")
pret_masini = {
    'Dacia': 6800,
    'Lastrun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget_client = 15000

for marca, pret in pret_masini.items():
    if buget_client >= pret:
        print(f"Puteti alege masina {marca} cu pretul {pret}")

'''
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
print("Ex 7")
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count_3 = 0
for numar in numere:
    if numar == 3:
        count_3 += 1
print(f"Numarul '3' apare de {count_3} ori")

'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''

print("Ex 8")
s = 0
for numar in numere:
    s += numar
print(f"Suma numerelor este {s}")

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
print("Ex 9")
maxim = numere[0]
for numar in numere:
    if maxim < numar:
        maxim = numar
print(f"Cel mai mare numar din lista este {maxim}")

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
'''
print("Ex 10")
for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(f"Lista noua cu valorile pozitive modificate in negative este {numere}")

print("Exercitii Optionale")
'''
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
print("Ex 1")
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
numere_0 = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 != 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
    if numar == 0:
        numere_0.append(numar)
print(f"Lista cu numere pare sunt {numere_pare}")
print(f"Lista cu numere impare sunt {numere_impare}")
print(f"Lista cu numere pozitive sunt {numere_pozitive}")
print(f"Lista cu numere negative sunt {numere_negative}")
print(f"Lista cu numere 0 sunt {numere_0}")


'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
print("Ex 2")
for i in range(0, len(alte_numere)):
    for j in range(0, len(alte_numere) - i - 1):
        if alte_numere[j] > alte_numere[j + 1]:
            alte_numere[j], alte_numere[j + 1] = alte_numere[j+1], alte_numere[j]
print(f"Lista sortata cu bubble sort este: {alte_numere}")

'''
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
print("Ex 3")
# numar_ghicit = None
while True:
    numar_secret = random.randint(1, 31)
    # numar_ghicit = 0
    numar_ghicit = int(input("Introduceti numarul secret: \n"))
    if numar_ghicit > numar_secret:
        print(f"Numar ghicit {numar_ghicit} este mai mare decat numar secret {numar_secret}")
    elif numar_ghicit < numar_secret:
        print(f"Numar ghicit {numar_ghicit} este mai mic decat numar secret {numar_secret}")
    elif numar_ghicit == numar_secret:
        print(f"Felicitari! Ai ghicit! Numerul ghicit {numar_ghicit} si Numar secret {numar_secret} sunt egale")
    break

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
print("Ex 4")
numar = 7
for i in range(1, numar + 1):
    for j in range(1, i + 1):
        print(i, end="")
    print()

'''
5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
print("Ex 5")
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for numar in tastatura_telefon:
    for cifra in numar:
        print(f"Cifra curenta este: {cifra}")