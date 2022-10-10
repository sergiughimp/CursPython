
'''
Numele de clasa se scrie mereu cu litera mare de la inceput
'''


class Burger:

    def __init__(self, ingrediente, sos, vegetarian=False):
        self.ingrediente = ingrediente
        self.sos = sos
        self.vegetarian = vegetarian

    def reteta(self):
        print("Prajiti chifla")
        print("Puneti partea de jos a chiflei pe o farfurie")
        if self.vegetarian:
            print("Adaugati o bucata prajita de halloumi")
        else:
            print("Adaugati o bucata de vita augus")
        for ingredient in self.ingrediente:
            ingredient.gateste()
            # print(f"Adaugati {ingredient}")
        print(f"Turnati mult {self.sos} peste ingrediente")
        print(f"Puneti partea de sus a chiflei peste burget")
        print("Serviti cald!")


class Ingredient:

    def __init__(self, nume, metoda_gatire):
        self.nume = nume
        self.metoda_gatire = metoda_gatire

    def gateste(self):
        print(f"Ingredient: {self.nume}")
        print(f"\t{self.metoda_gatire}")


ingredient1 = Ingredient("Cheddar", "taiati in felii si puneti peste burger")
ingredient2 = Ingredient(
    "Ceapa", "prajiti in ulei pana devine dulce, apoi puneti peste burger")
ingredient3 = Ingredient(
    "Castraveti murati", "deschideti borcanul, taiati castravetii felii si puneti peste burger")
ingredient4 = Ingredient("Rosii", "taiati felii si puneti peste burger")

# new_burger1 = Burger(["cheddar", "rosii", "ceapa", "castraveti murati"], "BBQ")
new_burger1 = Burger([ingredient1, ingredient2, ingredient3], "BBQ")
new_burger1.reteta()

print("*"*90)

# new_burger2 = Burger(["rosii", "ceapa", "avocado"], "Remoulade", True)
new_burger2 = Burger(
    [ingredient1, ingredient4, ingredient3], "Remoulade", True)
new_burger2.reteta()
