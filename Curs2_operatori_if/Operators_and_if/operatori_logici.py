# avem 3 operatori logici (functioneaza doar pe variabile boolean): and not or
# and - conditie de tip SI: x and y -> atat x si y sa fie adevarat
driver_licence = True
varsta = 21

# and - ambele conditii adevarate pentru ca rezultatul sa fie adevarat
assert driver_licence and varsta > 18, "nu ai voie sa conduci o masina"

nota1, nota2, nota3 = 7, 5, 8
assert nota1 > 4 and nota2 > 4 and nota3 > 4, "Ai picat"

nota1, nota2, nota3 = 3, 2, 3
# or - x sau y: adevarat daca cel putin unul dintre conditiile x sau y este adevarata
assert nota1 < 4 or nota2 < 4 or nota3 < 4, "Ai trecut"

# not - operatorul de negare -> transforma True in False si False in True
major = varsta > 18
print(major)
print(not major)