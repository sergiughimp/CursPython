'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Deptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}")

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return self.latime + self.lungime / 2

    def schimba_culoare(self, culoare_noua="galben"):
        print(f"Dreptunghiul isi schimba culoare in {culoare_noua}")
        self.culoare = culoare_noua

dreptunghi1 = Dreptunghi(34, 20, "verde")
dreptunghi1.descrie()
print(f"Dreptunghiul are aria: {dreptunghi1.aria()}")
print(f"Dreptunghiul are perimetru: {dreptunghi1.perimetru()}")
dreptunghi1.schimba_culoare()
dreptunghi1.descrie()