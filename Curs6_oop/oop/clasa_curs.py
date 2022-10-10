from clasa_person import Person

'''
clasa = concept, suma de caracteristici (atribute) si actiuni (metode)
'''
class CursProgramare:
    def __init__(self, companie, nume, durata, data_inceput, numar_locuri=10):
        self.companie = companie
        self.nume = nume
        self.durata = durata
        self.data_inceput = data_inceput
        self.numar_locuri_disponibile = numar_locuri
        self.studenti = []

    def inscriere_student(self, student):
        # Aici verificam daca a trecut data de inceput, si daca nu, sa inscriem studentul
        if self.numar_locuri_disponibile > 0:
            self.studenti.append(student)
            self.numar_locuri_disponibile -= 1
            print(f"Studentul {student.nume} {student.prenume} a fost inscris cu succes!")
        else:
            print(f"Ne pare rau, nu mai sunt locuri disponibile")

    def descriere_curs(self):
        print(f"{self.nume}[{self.companie}] - {self.durata} zile")
        print("-"*80)
        for student in self.studenti:
            print(f"{student.nume} {student.prenume} ({student.varsta})")
        if not self.studenti:
            print("Nu sunt deloc stundeti inscrisi")
        print()

curs_python = CursProgramare("IT factory", "Introducere in Python", 120, "2023-01-01")
curs_python.descriere_curs()

# new_person1 = Person("Suciu", "Mihai", 22, 1.70)
# new_person2 = Person("Chetves", "Florian", 23, 1.80)
#
# curs_python.inscriere_student(new_person1)
# curs_python.inscriere_student(new_person2)
# curs_python.descriere_curs()
#
# curs_python.inscriere_student(
#     Person("Lazarica", "Petrut", 43, 1.55)
# )
# curs_python.inscriere_student(
#     Person("Briceag", "Marcela", 21, 1.45)
# )
# curs_python.descriere_curs()