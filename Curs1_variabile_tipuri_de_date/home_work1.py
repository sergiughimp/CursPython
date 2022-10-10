'''
Ex 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''
# variable = container for storing values
'''
Ex 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
name = "Sergiu"
age = 26
height = 1.83
married = False

'''
Ex 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print(type(name))
print(type(age))
print(type(height))
print(type(married))

'''
Ex 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
height = round(height)
print(height, type(height))

'''
Ex 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print(f"My name is {name}, I'm {age} years old, my height is {height} and my marriage status is {married}")

'''
Ex 6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
# first_name = input("My first name is \n")
# last_name = input("My last name is \n")
# print(f"My full has {len(first_name) + len(last_name)} characters")


'''
Ex 7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
length = 34
width = 26
aria = length * width
print(f"Aria dreptunghiului este {aria}")

'''
Ex 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';

Ex 9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''
string = "Coral is either the stupidest animal or the smartest rock2"
print(string.count(" the "))

string = 8

'''
Ex 10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''
s = "4444"
# assert 42 == int(s), "nu contine doar numere"
assert s.isdigit(), "nu contine doar numere"
assert s.isnumeric(), "nu contine doar numere"

'''
Exercitii optionale
Ex 1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
# string = input("Introdu un string de dimensiune impara: \n")
last_name = "ghimp"
for i in range(0, len(last_name)):
    if i == int(len(last_name) / 2):
        print(last_name[i])
'''
Ex 2. Folosind assert, verifică dacă un string este palindrom.
'''
palindrom = "madam"
assert palindrom == palindrom[::-1], "nu este palindrom"

'''
Ex 3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
string = 'alabala portocala'
first_string1, second_string1 = "alabala", "portocala"
first_string2, second_string2 = string.split()
print(first_string1)
print(first_string2)
print(second_string1)
print(second_string2)

'''
Ex 4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla
'''
string1 = 'alabala portocala'
first = string[0]
for i in range(1, len(string1)-1):
    if string1[i] == first:
        upper = string1[i].upper()
        replace = string1.replace(string1[i], upper)
print(string1[0] + replace[1:-1] + string1[-1])

'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''
# Ex5
# user = input("Introduceti un user: \n")
# password = input("Introceti o parola: \n")
# print(f"Parola pentru user {user} este {password.replace(password,'*'*len(password))} si are {len(password)} caractere")