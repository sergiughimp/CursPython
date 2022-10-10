
'''
O clasa =  sablon pe care il folosim ca sa cream 'obiecte' din acea clasa.
Obiecte = au 2 proprietati importante:
    - caracteristici = (pe care in clasa le numim ATRIBUTe)
    - metode = adica functiile definite in interiorul clasei care ne zic noua ce pot face obiectele
'''
class Person:
    # nume = ""
    # prenume = ""
    # varsta = 0
    # inaltime = 0.0

    '''
    Metoda speciala init = folosita ca si punt de intrare pentru creare de obiecte
    '''
    def __init__(self, last_name, first_name, age, height):
        self.nume = last_name
        self.prenume = first_name
        self.varsta = age
        self.inaltime = height
    # self = cuvant cheie care reprezinta obiectul la care ne referim la momentul apelarii metodei

    def present_me(self):
        print(f"Salut, eu sunt {self.nume} {self.prenume} si am {self.varsta} ani")

    def creste_varsta(self):
        self.varsta += 1
        print(f'Peste un an {self.nume} {self.prenume} a ajuns la varsta de {self.varsta} ani')
'''
new_Peson1 si new_Person2 sunt obiecte create din clasa Person
'''
new_Person1 = Person('Popescu', 'Maria', 18, 1.82)
new_Person2 = Person('Marinescu', 'Petru', 24, 1.54)
new_Person3 = Person('Ionescu', 'Gigi', 34, 1.68)

'''
deoarece am folosit clasa Person ca si sablon pentru a aceste obiecte, putem apela metoda present_me pe ambele
'''
# new_Person1.present_me()
# new_Person2.present_me()
# new_Person3.present_me()

persoane = [new_Person1, new_Person2, new_Person3]
# new_Person3.creste_varsta()

# print("*" * 110)
# for person in persoane:
#     person.present_me()
#     person.creste_varsta()
