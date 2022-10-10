from pprint import pprint
# dictionar  =  stuctura de date care stocheaza informatii in perechi cheie-valoare unde cheile actioneaza ca si indici de la lista, adica ne permit sa ne referim la valori bazat pe chei

dict_gol = {}

dict1 = {
    "s": 12,
    3: 45,
    3.14: "un alt string",
    True: 5,
    "x": False
}

tren = ["grau", "orz", "orez", "hrisca", "quinoa", "porumb"]
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru": ["orez", " amaranth"],
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
}

# cheile din dictionar trebuie sa fie unice
# cheile trebuie sa fie tipuri de date simple(int, float, bool, string)
pprint(tren_colorat)
print(f"in vagonul rosu avem {tren_colorat['rosu']}")
print(f"in vagonul albastru avem {tren_colorat['albastru'][0]} si {tren_colorat['albastru'][1]}")


# exemplu: de cate ori apare litera in cuvant
cuvant = "abracadabra"
# daca facem asa, vom avea nevoie de 26 de variabile...cam multe
litera_a_cnt = cuvant.count("a")
litera_b_cnt = cuvant.count("b")

# facem un dictionar in care cheia este litera cautata, iar valoare este de cate ori apare in text
dict_litere_cnt = {
    "a": cuvant.count("a"),
    "b": cuvant.count("b"),
    "r": cuvant.count("r"),
}
print(dict_litere_cnt)

# exemplu: grupare date in mod logic
student_name = "Popescu"
student_firstname = "Ion"
student_age = 21
student_weight = 76.5

student = {
    "name": "Popescu",
    "firstname": "Ion",
    "age": 21,
    "weight": 76.5,
    "birthdate":{
        "day": 19,
        "month":"June",
        "year": 1991
    }
}
print(f"Ma cheama {student['name']} {student['firstname']}. Am {student['age']} ani si {student['weight']} kg")
print(f"M-am nascut pe {student['birthdate']['year']}, {student['birthdate']['day']} {student['birthdate']['month']}")


birthdate = student['birthdate']
print(f"M-am nascut pe {birthdate['day']} {birthdate['month']} {birthdate['year']} ")


# operatii pe dictionare
tren_colorat = {
    "rosu": "grau",
    "verde": "orz",
    "albastru":  "amaranth",
    "galben": "hrisca",
    "alb": "quinoa",
    "negru": "porumb",
}
# adaugare element: folosim o cheie care nu mai exista si elementul e agaugat
tren_colorat['roz'] = "naut"
pprint(tren_colorat)

# stergere element
del tren_colorat['roz']
pprint(tren_colorat)

# modificare element
tren_colorat['rosu'] = "pietre"
print(tren_colorat)

# pentru a schimba cheia, trebuie sa adaugam un nou element cu noua cheia si sa stergem pe cea veche
pietre = tren_colorat['rosu']
del tren_colorat['rosu'] # va sterge pietre
tren_colorat['turcoaz'] = pietre
pprint(tren_colorat)

# Values se pot repeta, nu trebuie sa fie unice
tren_colorat['maro'] = 'orz'
tren_colorat['magenta'] = 'orz'

# Daca cheia nu este in dictionar cu adresare directa, vom primit eroare
print(tren_colorat)
# print(tren_colorat['portocaliu']) # eroare, nu este nici un vagon portocaliu

if 'portocaliu' in tren_colorat: # pot testa daca o key este in dictionar sau nu
    print(tren_colorat['potocaliu'])
else:
    print("nu este niciun vagon portocaliu")