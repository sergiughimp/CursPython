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
# Exercitiu optional
import random

jucatori = ['J1', 'J2', 'J3', 'J4', 'J5']
schimbari_efectuate = 0
schimbari_maxim = 3
random.shuffle(jucatori)

print(f"Lista initiala de jucatori este {jucatori}")

while 0 < schimbari_maxim <= 3:
    raspuns_user = input("Doresti sa faci o schimbare in lista de jucatori? (da/nu?)\n")
    if raspuns_user.lower() == "da":

        jucator_out = input("Ce jucator doresti sa fie eliminat din lista de jucatori? \n")
        while jucator_out not in jucatori:
            print(f"Jucatorul {jucator_out} nu exista in lista de jucatori")
            jucator_out = input("Alege alt jucator pentru a fi eliminat \n")

        jucatori.remove(jucator_out)
        print(f"Jucatorul {jucator_out} a fost eliminat din lista de jucatori")

        jucator_in = input("Ce jucator doresti sa introduci in lista de jucatori? \n ")
        while jucator_in in jucatori:
            print(f"Jucatorul {jucator_in} este deja in lista de jucatori")
            jucator_in = input("Alege alt jucator pentru a fi introdus \n")

        jucatori.append(jucator_in)
        print(f"Jucatorul {jucator_in} a fost introdus in lista de jucatori")

        schimbari_maxim -= 1
        schimbari_efectuate += 1

        print(f"Schimbarea s-a facut cu succes intre jucatorul {jucator_out} si jucatorul {jucator_in}")
        print(f"Lista finala de jucatori dupa {schimbari_efectuate} schimbari efectuate este: {jucatori}")

    elif raspuns_user.lower() == "nu":
        print(f"Nu s-a efectuat nicio schimbare in lista de jucatori.")
        print(f"Lista finala de jucatori este: {jucatori}")

    else:
        print("Pentru a face o schimbare trebuie sa raspunzi cu 'Da' sau 'Nu'.")

