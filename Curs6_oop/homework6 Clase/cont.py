'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
from angajat import Angajat
class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        print(f"Titularul {self.nume} {self.prenume} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.suma = suma
        return self.sold + self.suma

    def credidare_cont(self, suma):
        self.suma = suma
        return self.sold - self.suma
    
angajat1 = Angajat("Popescu", "Maria", 3200)
angajat2 = Angajat("Ionescu", "Ioana", 3200)
cont1 = Cont("RO4214", angajat1.nume, 10)
cont2 = Cont("RO1234", angajat2.nume, 50)
cont1.afisare_sold(angajat1.nume, angajat1.prenume)
cont2.afisare_sold(angajat2.nume, angajat2.prenume)
print(f"Suma titularului {angajat1.nume} {angajat1.prenume} dupa debitare este {cont1.debitare_cont(2)}.")
print(f"Suma titularului {angajat1.nume} {angajat1.prenume} dupa creditare este {cont1.credidare_cont(2)}.")