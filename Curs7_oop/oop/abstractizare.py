'''
Pilonii OOP: inheritance (mostenirea), abstraction (abstractizarea), polymorphism (polimorfism), encapsulation (incapsularea)
2. abstraction (abstractizare)
    -> ca si mosternirea, dar clasa parinte este o clasa abstracta, adica nu putem face obiecte din ea, si o folosim doar ca si un template pentru metodele pe care ar trebui sa le implementeze copii
    -> clasa abstracta trebuie sa mosteneasca clasa ABC (from abc import ABC)
    -> fiecare metoda a clasei abstracte trebuie sa arunce exceptia
    -> clasa abstracta Nu are constructor, deoarece nu putem face obiecte abstracte

3. Polimorfism -> poli (mai multe) morifs (forme)
    -> ceva care poate lua mai multe forme
    -> o functie care desi are acelasi nume, are implementari diferite
    (Ex: aria() -> Dreptunghi, aria() -> Cerc)
    (Ex: perimetru() -> Dreptunghi, perimetru() -> Cerc)
'''
import math
from abc import ABC


class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormaGeometrica):

    def aria(self):
        return self.raza ** 2 * 3.14

    def perimetru(self):
        return self.raza * 3.14

    def __init__(self, raza):
        self.raza = raza


class Dreptunghi(FormaGeometrica):
    def aria(self):
        return self.lat1 * self.lat2

    def perimetru(self):
        return (self.lat1 + self.lat2) * 2

    def diagonala(self):
        return math.sqrt(self.lat1 ** 2 + self.lat2 ** 2)

    def __init__(self, lat1, lat2):
        self.lat1 = lat1
        self.lat2 = lat2


cerc1 = Cerc(10)
dreptunghi1 = Dreptunghi(4, 6)
print(cerc1.aria())
print(dreptunghi1.aria())

print(cerc1.perimetru())
print(dreptunghi1.perimetru())


# -------------------------------------------------------
lista_figuri_geometrice = [Cerc(4), Dreptunghi(2, 7), Dreptunghi(5, 6), Dreptunghi(9, 7), Cerc(12)]
for fg in lista_figuri_geometrice:
    print("*"*80)
    print(f"Perimetru: {fg.perimetru()}")
    print(f"Aria: {fg.aria()}")