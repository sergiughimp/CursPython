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

    __latura = 10

    def __init__(self, nume):
        self.nume = nume

    def getter_latura(self):
        return self.__latura

    def setter_latura(self, noua_latura):
        self.__latura = noua_latura

    def deleter_latura(self):
        pass

    def aria(self):
        return self.__latura * self.__latura

class Cerc(FormaGeometrica):

    __raza = 12

    def __init__(self, nume):
        self.nume = nume

    def getter_raza(self):
        return self.__raza

    def setter_raza(self, noua_raza):
        self.__raza = noua_raza

    def aria(self):
        return self.__raza ** 2 * 3.14

    def descrie(self):
        print("Eu nu am colturi")

patrat = Patrat("Patrat")
cerc = Cerc("Cerc")

print(f"Aria patratului inainte de modificare este: {patrat.aria()}")
patrat.descrie()
patrat.setter_latura(4)
print(f"Aria patratului dupa modificare este: {patrat.aria()}")

print("*"*50)

print(f"Aria cercului inainte de modificare este: {cerc.aria()}")
cerc.descrie()
cerc.setter_raza(2)
print(f"Aria cercului dupa modificare este {cerc.aria()}")
