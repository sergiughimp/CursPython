'''
3. Clasa Angajat
Atribute: nume, prenume, salariu, daca e cu contract
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''

class Angajat:

    # toti parametri constructorului (in afara de self) reprezinta atribute cu care construim un obiect
    def __init__(self, nume, prenume, salariu, contract=True):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.contract = contract

    def descrie(self):
        print(f"Nume: {self.nume}")
        print(f"Prenume: {self.prenume}")
        print(f"Salariu: {self.salariu}")
        if self.contract:
            print(f"Contract")
        else:
            print(f"Fara contract")

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu += (procent * self.salariu) / 100
        return self.salariu

angajat1 = Angajat("Popescu", "Ion", 1200)
angajat2 = Angajat("Ionescu", "Gheorghe", 1500, contract=False)

angajat1.descrie()
print(f"Angajatul1 are salariu anual {angajat1.salariu_anual()}")
print(f"Salariu angajatului1 dupa marire este {angajat1.marire_salariu(15)}")
print("*"*100)
angajat2.descrie()
print(f"Angajatul2 are salariu anual {angajat2.salariu_anual()}")
print(f"Salariu angajatului2 dupa marire este {angajat2.marire_salariu(10)}")
