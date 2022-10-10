
# declararea Array
elevi = ['Gigle', 'Costel', 'Mari', 'Ela', 'Ada']
numere = [1, 33, 81, 99, 201]
# contine mai multe elemente de acelasi tip
# accesam elemetele prin index care incepe de la 0
# are o dimensiune fixa
# are proprietatea len care ne da dimensiunea array-ului
print(f'Afisarea array-ului initial: {elevi}')
print(f'elementul de pe pozitia 1 este: {elevi[1]}')  # afisarea elementului de pe pozitia index-ului 1
elevi[1] = 'Sebi' # suprascrierea elementului de pe pozitia 1
print(f'elementul de pe pozitia 1 s-a modificat in: {elevi[1]}')
print(f'lungimea array-ului este: {len(elevi)}')
print(f'Afisarea array-ului dupa modificare: {elevi}')
print(f'Afisarea ultimului element din array: {elevi[len(elevi) - 1]}')