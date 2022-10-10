'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul cu numele {self.nume} si cu prenumele {self.prenume} are salariul {self.salariu} lei")

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return str(self.salariu) + ' lei'

    def salariu_anual(self):
        return str(self.salariu * 12) + ' lei'

    def marire_salariu(self, procent):
        self.procent = procent
        if procent == 10:
            return self.salariu + self.salariu * 0.1
        elif procent == 20:
            return self.salariu + self.salariu * 0.2
        elif procent == 30:
            return self.salariu + self.salariu * 0.3
        elif procent == 40:
            return self.salariu + self.salariu * 0.4
        elif procent == 50:
            return self.salariu + self.salariu * 0.5
        elif procent == 60:
            return self.salariu + self.salariu * 0.6
        elif procent == 70:
            return self.salariu + self.salariu * 0.7
        elif procent == 80:
            return self.salariu + self.salariu * 0.8
        elif procent == 90:
            return self.salariu + self.salariu * 0.9

angajat0 = Angajat("Popescu", "Maria", 3200)
angajat0.descrie()
print(f"Numele complet al angajatului este: {angajat0.nume_complet()}")
print(f"Salariu lunar al anagajatului este: {angajat0.salariu_lunar()}")
print(f"Salariu anual al angajatului este: {angajat0.salariu_anual()}")
print(f"Salariul marit al angajatului este: {angajat0.marire_salariu(10)}")
print("*"*100)