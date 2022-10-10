'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

import math
class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f"Culoare cercului este: {self.culoare}")
        print(f"Raza cercului este: {self.raza}")

    def aria(self):
        return round(math.pi * self.raza, 2)

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return round(math.pi * self.raza * 2, 2)

cerc1 = Cerc(4, "verde")
cerc2 = Cerc(8, "albastru")

cerc1.descriere_cerc()
print(f"Aria cercului este: {cerc1.aria()}")
print(f"Diametru cercului este: {cerc1.diametru()}")
print(f"Circumferinta cercului este: {cerc1.circumferinta()}")
print("*"*80)
cerc2.descriere_cerc()
print(f"Aria cercului este: {cerc2.aria()}")
print(f"Diametru cercului este: {cerc2.diametru()}")
print(f"Circumferinta cercului este: {cerc2.circumferinta()}")