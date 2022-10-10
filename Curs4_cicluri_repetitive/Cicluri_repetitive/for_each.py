note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# for index in range(len(note_muzicale)):
#     print(f"La indexul {index} am gasit nota muzicala {note_muzicale[index]}")
#
# print('*' * 150)
# # for each
# # for element din colectie
# #       facem ceva cu elementul respectiv
# # unde colectie = lista, set, dictionar, tupla
#
# for nota in note_muzicale:
#     print(f"Nota curenta este {nota}")
#
# print('*' * 150)
# # vreau sa aflu de cate ori apare nota do in lista, fara sa folosesc count
# count_do = 0
# for nota in note_muzicale:
#     print(f"Acum testez nota {nota}...")
#     if nota == 'do':
#         count_do += 1
#         print(f"    Am gasit un 'do', contorul a ajuns acum la {count_do}")
# print(f"Am gasit nota 'do' in lista de note muzicale de {count_do} ori")
#
# # Problema: vreau sa gasesc cu nota 'x'(nota primita de la utilizator) in note_muzicale. Daca o gasesc, vreau sa ma opresc prima data cand am gasit-o. Daca nu exista in lista, vreau sa afisez ca nu exista in lista.

# # break - for-ul se opreste automat cand intalneste break, chiar daca mai exista elemente in colectie
# nota_cautata = input("Introduceti nota cautata: \n")
# gasit = False # flag pentru a sti daca am gasit ce cautam sau nu
#
# for nota in note_muzicale:
#     print(f"Acum testam nota {nota}...")
#     if nota == nota_cautata:
#         print(f"Am gasit nota cautata")
#         gasit = True
#         break
# if not gasit:
#     print(f"Nu am gasit deloc nota cautata")
# print(f"Am terminat bucla de cautare")

# Varianta 2
# nota_cautata = input("Introduceti nota cautata: \n")
#
# for nota in note_muzicale:
#     print(f"Acum testam nota {nota}...")
#     if nota == nota_cautata:
#         print(f"Am gasit nota cautata")
#         break
# else:
#     # aici se ajunge doar daca for-ul a ajuns la final fara sa dea de vreun break
#     print("Nu am gasit nota cautata")


# For-else
# atunci cand folosim break intr-un for, putem avea si ramura else pentru for care va fi executata doar daca for-ul a rulat fara sa ajunga deloc la break

# continue - da skip (va sari pentru iteratia respectiva)

# vreau sa printez toate notele muzicale, mai putin cele care incep cu s
print(f"Notele muzicale ca nu incep cu s sunt: ")
for nota in note_muzicale:
    if nota[0] == 's':
#         sari peste aceasta nota, nu vreau sa o printez, deoarece incepe cu s
        continue
    print(nota)

# vreau sa afisez numerele mai mici ca 10 care nu sunt divizibile cu 3
for index in range(10):
    if index % 3 == 0:
        continue
    print(f"Numarul {index} nu este divizibil cu 3")