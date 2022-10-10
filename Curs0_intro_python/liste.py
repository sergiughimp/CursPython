lista1 = [1, 33, 'Mari', 99, 'Ana']
fructe = []
print(f'Afisare lista1: {lista1}')
print(f'Afisarea lista2 goala: {fructe}')
fructe.append('banana')
fructe.append('orange')
fructe.append('mar')
fructe.append(1)
fructe.append(True)
fructe.append(1)
print(f'Afisarea lista fructe dupa adugarea de elemente: {fructe}')
fructe[0] = 'para' # suprascriere
print(f'Afisarea lista fructe dupa modificarea elementului de pe pozitia 0: {fructe}')
print(f'Afisarea indexului elementului banana din lista fructe: {fructe.index("mar")}')
print(f'Afisarea dimensiunea listei fructe: {len(fructe)}')
print(f'Afisarea ultimului element din lista: {fructe.pop()}')
print(f'Afisarea numarului de aparitii a elementului 1: {fructe.count(1)}')

fructe_exotice = ['ananas', 'kivi']
fructe.extend(fructe_exotice)
print(f'Afisarea listei fructe extinse: {fructe}')