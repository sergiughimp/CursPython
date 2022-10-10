# dalmatienii
for i in range(0, 15):
    print(f'Dalmatianul cu numarul: {i}')
# dalmatienii din 2 in 2
for i in range(0, 15, 2):
    print(f'Dalmatianul cu numarul: {i}')

# parcurgem lista cu for prin intermediul indexului

numere = [3, 7, 10, 20, 30]
# for i in range(0, len(numere)):
#     print(f'Numarul curent este {numere[i]}')

s = 0
for numar in numere:
    print(f'Numarul curent este: {numar}')
    s += numar
print(f'Suma este: {s}')

# de cate ori apare 3 in [3, 2, 3, 5, 3]
numere2 = [3, 2, 3, 5, 3]
count = 0
for numar in numere2:
    if numar == 3:
        count += 1
print(count)

# suma numerelor pare din aray
numere3 = [2, 5, 7, 4]
s = 0
for numar in numere3:
    if numar % 2 == 0:
        s += numar
print(s)