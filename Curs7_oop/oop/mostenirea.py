'''

Pilonii OOP: inheritance (mostenirea), abstraction (abstractizarea), polymorphism (polimorfism), encapsulation (incapsularea)
1. inheritance (mostenirea)
    -> clase care impartasesc atribute: in cazul aceste, putem face o clasa de baza (parinte) si apoi clase copil, care sa mosteneasca parintele si implicit toate atributele acestuia.
    -> permite sa avem o ierarhie a claselor, cu oricate nivele dorim
    -> se pot mosteni atat atribute, cat si metodele clasei parinte
    -> clasa copil poate avea in plus fata de clasa parinte oricate atribute sau oricate metode doreste
    -> in cazul metodelor, atunci cand avem in clasa copil o metoda exact ca si in clasa parinte zicem ca o suprascriem (overwrite), si TREBUIE sa fim atenti ca daca vrem sa beneficiem si de ceea ce se intampla in clasa parinte, sa o apelam cu super() -> exemplu in constructor

'''
# clasa parinte (de baza)
class Person:
    # atribut de clasa
    contor_persoane = 0

    def __init__(self, nume, varsta, adresa):
        Person.contor_persoane += 1
        self.nume = nume
        self.varsta = varsta
        self.adresa = adresa

    def descrie(self):
        print("*"*50)
        print(f"Nume: {self.nume}")
        print(f"Varsta: {self.varsta}")
        print(f"Adresa: {self.adresa}")

    def anul_nasterii(self):
        return 2022 - self.varsta

# clasa copil (mosteneste Person si implicit toate atributele acesteia)
class Student(Person):

    def __init__(self, nume, varsta, adresa, facultate, an_studiu):
        # super() reprezinta clasa parinte, in cazul nostru Person
        # aici apelam constructorul clasei parinte
        super().__init__(nume, varsta, adresa)
        self.facultate = facultate
        self.an_studiu = an_studiu

    def descrie(self):
        super().descrie()
        print(f"Facultate: {self.facultate}")
        print(f"An studiu: {self.an_studiu}")

    def anul_absolvirii(self):
        return 2022 + 4 - self.an_studiu

class Angajat(Person):

    def __init__(self, nume, varsta, adresa, companie, salariu):
        super().__init__(nume, varsta, adresa)
        self.companie = companie
        self.salariu = salariu

    def descrie(self):
        super().descrie()
        print(f"Companie: {self.companie}")
        print(f"Salariu: {self.salariu}")

    def salariu_anual(self):
        return self.salariu * 12

print(Person.contor_persoane)
student1 = Student("Ion", 21, "Cluj", "UTCN", 2)
angajat1 = Angajat("Gheorghe", 45, "Sibiu", "Continental", 2500)
print(Person.contor_persoane)

student1.descrie()
angajat1.descrie()

# metodele comune claselor copil vor fi puse in clase parinte (ca sa nu repetam codul)
print(f"Anul nasterii al studentului este: {student1.anul_nasterii()}")
print(f"Anul nasterii al angajatului este: {angajat1.anul_nasterii()}")

# metodele specificate fiecarului copil vor fi puse in clasa copil de care apartin
print(f"Anul absolvirii al studentului este: {student1.anul_absolvirii()}")
print(f"Salariul anual al angajatului este: {angajat1.salariu_anual()}")
