'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
'''
print("Ex 1")
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

if note_muzicale == note_muzicale[0: len(note_muzicale): 1]:
    note_muzicale = note_muzicale[len(note_muzicale)::-1]
    print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)

'''
2. De câte ori apare ‘do’?
'''
print("Ex 2")
print(note_muzicale.count("do"))

'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''
print("Ex 3")
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list3 = list1 + list2
list1.extend(list2)
if list3 == list1:
    print("Listele au fost concatenate cu succes")
else:
    print("Concatenare nereusita")

'''
4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
print("Ex 4")
list3.sort()
list3.remove(0)
print(list3)

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală
'''
print("Ex 5")
if list3:
    print(f"List is not empty")
else:
    print(f"List is empty")

'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
print("Ex 6")
list3.clear()
print(list3)

'''
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
print("Ex 7")
if list3:
    print(f"List is not empty")
else:
    print(f"List is empty")

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
print("Ex 8")
dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}
# print(dict1.keys())
for key, value in dict1.items():
    print(key)

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print("Ex 9")
for key, value in dict1.items():
    print(f"{key} are nota {value}")

'''
10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
print("Ex 10")
dict1["Dorel"] = "6"
print(dict1)

'''
11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
print("Ex 11")
del dict1["Gigel"]
dict1["Ionica"] = "9"
print(dict1)

'''
12. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
print("Ex 12")
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')
print(zile_sapt)

'''
13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.
'''
print("Ex 13")
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din saptamana")
else:
    print("Weekend nu este un subset al zilelor din saptaman")
'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
print("Ex 14")
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
print("Ex 15")
print(zile_sapt.intersection(weekend))
print(weekend.intersection(zile_sapt))

'''
Exerciții Opționale
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori
'''
print("Exercitiu optional")
import random

jucatori = ['J1', 'J2', 'J3', 'J4', 'J5']
count = len(jucatori)
schimbari_efectuate = 0
schimbari_maxim = 3
# lista amestecata random
random.shuffle(jucatori)

for item in jucatori[0: len(jucatori)]:
    # transforamam lista in set pentru a avea numai elemente unice
    jucatori = set(jucatori)
    if item:
        print(f"Jucatorul {item} este in teren")
        if schimbari_maxim > 0 and schimbari_maxim <= 3 and schimbari_efectuate < 3 and schimbari_efectuate >= 0:
            print("Efectuam schimbarea")
            schimbari_maxim -= 1
            schimbari_efectuate += 1
            count += 1
            # print(schimbari_maxim)
            # print(schimbari_efectuate)
            jucatori.remove(item)
            jucatori.add(f"J{count}")
            print(jucatori)
        else:
            print("Nu mai avem schimbari")
    else:
        print(f"Nu se poate efectua schimbare deoarece jucatorul {item} nu este in teren")
        print(f"Nu mai avem schimbari")
print(jucatori)