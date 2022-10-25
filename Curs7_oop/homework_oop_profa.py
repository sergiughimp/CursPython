'''
ABSTRACTION
+    Clasa abstractă FormaGeometrica
+    Conține un field PI=3.14
+    Conține o metodă abstractă aria (opțional)
    Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
    probabil am colturi’
'''
'''
INHERITANCE
    Clasa Pătrat - moștenește FormaGeometrica
    constructor pentru latură
'''
'''
ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

    Clasa Cerc - moștenește FormaGeometrica
    constructor pentru rază
    raza este proprietate privată
    Implementează getter, setter, deleter pentru rază
    Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''
'''
POLYMORPHISM
    Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    Creează un obiect de tip Patrat și joacă-te cu metodele lui
    Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''

from abc import ABC


class FormaGeometrica(ABC):
    pi = 3.14

    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print("Cel mai probabil am colturi")

class Patrat(FormaGeometrica):


    def __init__(self, latura):
        self.__lat = latura

    def aria(self):
        return self.__lat ** 2

    # getter
    @property
    def lat(self):
        return self.__lat

    @lat.setter
    def lat(self, new_lat):
        self.__lat = new_lat


patrat = Patrat(10)
print(f"Patratul are latura initiala {patrat.lat}")
print(f"Aria patratului inainte de modificare este: {patrat.aria()}")
patrat.lat = 12
print(f"Patratul are aria setata la {patrat.lat}")
print(f"Aria patratului dupa modificare este: {patrat.aria()}")


print("*"*50)
