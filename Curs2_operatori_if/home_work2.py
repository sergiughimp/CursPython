
'''
Ex 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
'''
# if...else -> block of code that have a condition, if condition is true it takes first execution of code else it takes second execution of code

'''
Ex 2. Verifică și afișează dacă x este număr natural sau nu.
'''
n = 1
if n > 0:
    print(f"Numarul natural este: {n}")

'''
Ex 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru
'''
if n > 0:
    print(f"Numarul pozitiv este: {n}")
    if n == 1:
        print(f"Numarul este neutru la inmultire")
elif n < 0:
    print(f"Numarul negativ este: {n}")
else:
    print(f"Numarul este neutru la adunare")

'''
Ex 4. Verifică și afișează dacă x este între -2 și 13.
'''
x = 34
if x > -2 and x < 13:
    print(f"Numarul {x} este in intervalul -2 si 13")
else:
    print(f"Numatul {x} nu este in intervalul -2 si 13")
'''
Ex 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
x, y = 10, 5
if x - y < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica decat 5")
else:
    print(f"Diferenta dintre {x} si {y} este mai mare decat 5")

'''
Ex 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
x = 25
if x not in range(5, 27):
    print(f"Numarul {x} este in intervalul 5 si 27")
else:
    print(f"Numatul {x} nu este in intervalul 5 si 27")
'''
Ex 7. x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
'''
x, y = 5, 7
if x == y:
    print(f"{x} si {y} sunt egale")
else:
    print(f"{x} si {y} nu sunt egale")
'''
8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x, y, z = 7, 5, 6
if x == y == z:
    print("Este un triunghi echilateral")
elif x == y != z or x == z != y or x != y == z:
    print("Este un triunghi isoscel")
else:
    print("Este un triunghi oarecare")

'''
Ex 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
'''
# caracter = input("Introduceti un caracter: \n")
caracter = "r"
if caracter == 'A' or caracter == 'a' or caracter == 'E' or caracter == 'e' or caracter == 'I' or caracter == 'i' or caracter == 'O' or caracter == 'o' or caracter == 'U' or caracter == 'u':
    print(f"Caracterul {caracter} este o vocala")
else:
    print(f"Caracterul {caracter} nu este o vocala")

'''
Ex 10.Transformă și printează notele din sistem românesc în >
    Peste 9 => A
    Peste 8 => B
    Peste 7 => C
    Peste 6 => D
    Peste 4 => E
    4 sau sub => F
'''
# nota = int(input("Introduceti nota: \n"))
nota = 3
if nota >= 9 and nota <= 10:
    print("A")
elif nota >= 8 and nota <= 9:
    print("B")
elif nota >= 7 and nota <= 8:
    print("C")
elif nota >= 6 and nota <= 7:
    print("D")
elif nota >= 4 and nota <= 6:
    print("E")
elif nota <= 4 and nota > 0:
    print("F")
else:
    print(f"Nota {nota} nu exista")

'''
Exercitii optionale
Ex 1. Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = 23454
if len(str(x)) >= 4 and str(x).isdigit():
    print(f"Numarul {x} contine cel putin 4 cifre")
else:
    print(f"Numarul {x} nu contine cel putin 4 cifre")

'''
Ex 2. Verifică dacă x are exact 6 cifre.
'''
if len(str(x)) == 6:
    print(f"Numarul {x} are exact 6 cifre")
else:
    print(f"Numatul {x} nu are exact 6 cifre")


'''
Ex 3. Verifică dacă x este număr par sau impar (x e int).
'''
if x % 2 == 0:
    print(f"Numarul {x} este numar par")
else:
    print(f"Numatul {x} nu este numar par")

'''
Ex 4. x, y, z (int) Afișează care este cel mai mare dintre ele?
'''
x, y, z = 3, 4, 6
if x > y and x > z:
    print(f"Numarul {x} este cel mai mare")
elif y > x and y > z:
    print(f"Numarul {y} este cel mai mare")
elif z > y and z > x:
    print(f"Numarul {z} este cel mai mare")

'''
Ex 5. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''
a, b, c = 13, 12, 14
if a + b >= c and b + c >= a and c + a >= b:
    print("Triunghiul este valid")
else:
    print("Triunghiul nu este valid")

'''
Ex 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
string = "Coral is either the stupidest animal or the smartest rock"
x = 1
print(string[:-x])

'''
Ex 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
'''
first5string = string[0:5]
last5string = string[len(string)-5: len(string)]
print(first5string + last5string)

'''
8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
'''
index0 = string.index("rock")
print(string[0:index0])

'''
Ex 9. Citește de la tastatura un string. Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''
string = "Coral is either the stupidest animal or the smartest roc"
first_character = string[0]
last_character = string[-1]
assert first_character.lower() == last_character.lower(), "Charaters are not the same"

'''
Ex 10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''
string = "0123456789"
print(string[0:len(string):2])
print(string[1:len(string):2])

'''
Exerciții Bonus
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''
from random import randint

x = int(input("Introdu un numar de la 1 la 6: \n"))
dice_roll = randint(1, 6)
if dice_roll > x:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {x} dar a fost {dice_roll}")
elif dice_roll < x:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {x} dar a fost {dice_roll}")
elif dice_roll == x:
    print(f"Ai ghicit. Felicitari! Ai ales {x} si a fost zarul {dice_roll}")