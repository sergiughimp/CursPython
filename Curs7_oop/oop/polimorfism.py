'''
Pilonii OOP: inheritance (mostenirea), abstraction (abstractizarea), polymorphism (polimorfism), encapsulation (incapsularea)

Polimorfism
    -> mai multe functii cu acelasi nume, dar comportament sau parametri diferiti

    -> Metoda language este polimorfica, deoarece returneaza lucruri diferite in functie de obiectul care o apeleaza, DAR numele metodei este mereu acelasi
'''

class Romania:
    def language(self):
        return "Romana"

class Franta:
    def language(self):
        return "Franceza"

inst_ro = Romania()
inst_fr = Franta()

print(f"Limba vorbita in Romania este: {inst_ro.language()}")
print(f"Limba vornita in Franta este: {inst_fr.language()}")

def add(a, b, c=0):
    return a + b + c
print(add(4, 8))
print(add(4, 8, 2))