'''
Parametri (input - date de intrare in functie) sunt niste nume pe care noi le folosim pentru variabilele pe care le transmitem functiei
'''

def say_hello_to(name):
    print(f"Hello {name}")

say_hello_to("Sergiu")
say_hello_to("Marcela")
say_hello_to("Mihai")

def say_goodbye(name, age):
    print(f"Hi {name} with {age} years old")

say_goodbye("Maria", 24)
say_goodbye("Ionel", 25)
say_goodbye(52, "Ionel")
say_goodbye(age=52, name="Ionel") # zicem ca avem parametr numiti

print("*" * 110)
# atunci cand pentru anumiti parametri dorim sa avem valori prestabilite (default), putem face asta punand o valoare direct atunci cand definim functia

# def nume_functie(parametru=valoare):

# Daca oferim o valoare prestabilita, atunci parametrul nostru zicem ca este optional. Adica putem apela cu
# nume_functie()
# nume_functie(alta_valoare)

def say_hi(nume, mesaj="acesta este un mesaj standard!"):
    print(f"{mesaj}")
    print(f"I-am zis hi lui {nume}")

say_hi("Mihai")
say_hi("Mihai", "Alt mesaj")
say_hi("Johnny")
say_hi("Cineva")

'''
parametri 'traiesc' doar in interiorul functiei
la fel si orice variabila definita in interiorul functiei
'''

'''
Important: desi putem avea oricat parametri vrem noi intr-o functie, nu este recomandat sa avem mai multi de 6
'''
