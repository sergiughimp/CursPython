# # while - ciclu repetitiv in care nu stim exact numarul de pasi, dar stim exact ca avem o conditie de indeplinit
# # while = cat timp
#
# # while conditie:
# #   fa ceva
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1 # daca nu incrementam noi i-ul, programul va crash-ui deoarece bucla se va tot repeta pana ramane fara memorie
#
# '''
# in viata reala, folosim while atunci cand nu stim exact cat timp  trebuie sa executam un cod, dar avem o conditie de oprire
# - validarea unui input de la utilizator
# - validare user/parola
# - pentru a forta un numar maxim de incercari pentru o anumita actiune
# '''
# age_is_correct = False
# while not age_is_correct:
#     age = int(input("Varsta dvs: \n"))
#     if 1 < age < 99:
#         age_is_correct = True
#     else:
#         print("Varsta nu este corecta, incercati intre 1 si 99. Incercati din nou!")


# while-else functioneaza la fel ca si for-else. pe ramura else se va ajunge doar daca while-ul se termina si nu a ajuns deloc la un break
user, parola = "adela", "1111"
print("Nu sunteti logat. Trebuie sa va logati")
nr_incercari = 0
nr_max_incercari = 3
while nr_incercari < nr_max_incercari:
    my_password = input("Introduceti parola dvs:\n")
    if parola == my_password:
        print("Felicitari, sunteti logat cu succes")
        break
    else:
        print("Parola nu este corecta, incercati din nou")

    nr_incercari += 1
    print(f"Ai incercat sa te loghezi de {nr_incercari} ori")
    print(f"Mai ai {nr_max_incercari - nr_incercari} incercari ramase...")
else:
    # no-break
    print(f"Ai incercat  de 3 ori sa te loghezi gresit, nu mai ai voie sa incerci timp de 1 minut!")
print("Am terminat cu logarea")