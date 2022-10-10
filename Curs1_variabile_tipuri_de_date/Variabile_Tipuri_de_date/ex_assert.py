# assert = folosim pentru a verifica o anumita conditie
# daca conditia este adevarata, codul merge mai departe
# daca conditia este falsa, codul se opreste si da eroare
year_born = 1991
age = 31

# verificam daca anul nasterii e introdus corect in raport cu varsta
assert 2022 - year_born == age

year_born = 1991
age = 38
# punem dupa virgula un mesaj personalizat, ca sa stim ce nu a mers bine
# assert 2022 - year_born == age, f"Year born is {year_born} and it doesn't match with the age {age}"

# exemplu cu type casting si verificare cu variabila noua este integer
s1 = "42"
my_int = int(s1)
assert my_int == 42, f"{my_int} nu este un integer egal cu 42"