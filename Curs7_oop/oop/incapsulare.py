'''
Pilonii OOP: inheritance (mostenirea), abstraction (abstractizarea), polymorphism (polimorfism), encapsulation (incapsularea)

4. encapsulation (incapsularea)
    -> posibilitatea de a PROTEJA atributele clasei, folosind modificatorii de vizibilitate:
        -> private: atributul poate fi accesat doar din interiorul clasei in care a fost definit. Se definieste cu "__" in fata
        -> protected: atributul poate fi accesat din clasa in care a fost definit, dar si in clasele copul ale acesteia, insa nu poate fi accesat din exterior. Se defineste cu "_" in fata

-> Atunci cand avem un atribut ascuns (private), putem folosi niste metode speciale pentru a interactiona cu el, numite: getter -> pentru al vedea si setter -> pentru a-i schimba valoarea

-> in general, merodele acestea se vor denumi cu set_ / get_ + numele initial al varibilei:

clasa X:

    __ceva

    def get_ceva(self):
        return __ceva

    def set_ceva(self, ceva_nou):
        __ceva = ceva_nou
'''

'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''

class Factura:

    # atributele de clasa, daca modificam o data, modificam pentru TOATE obiectele
    __seria = "XYZ" # atributele cu 2 underscore in fata sunt private
    numar = 1

    def __init__(self, nume_produs, cantitate, pret_bucata):
        self.nr_fact = Factura.numar
        self.produs = nume_produs
        self.cant = cantitate
        self.pret = pret_bucata
        Factura.numar += 1

    # getter
    def get_seria(self):
        return self.__seria

    # setter
    def schimba_seria(self, noua_serie):
        # aici putem face validari, de exemplu: seria sa fie de minim 3 si maxim 6 caractere
        if 3 <= len(noua_serie) <= 6:
            self.__seria = noua_serie
        else:
            print("Nu e buna seria, mai incearca")

    def descrie(self):
        print(f"{self.__seria} {self.nr_fact}")
        print("*"*50)
        print(f"Produs | Cantitate | Pret unitar | Pret total")
        print(f"{self.produs} | {self.cant} | {self.pret} | {self.cant * self.pret}")

factura1 = Factura("Telefon", 10, 120)
# print(factura1.__seria, factura1.nr_fact)

factura2 = Factura("TV", 5, 70)
# print(factura2.__seria, factura2.nr_fact)
# print(factura1.__seria, factura1.nr_fact)
# print("*"*60)
# Factura.seria = "ABC"
# print(factura2.seria, factura2.nr_fact)
# print(factura1.seria, factura1.nr_fact)
factura1.descrie()
factura1.schimba_seria("ABC")
factura1.descrie()