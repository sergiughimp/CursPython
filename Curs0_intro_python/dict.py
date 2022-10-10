# declaram si initializam o lista goala
lista_goala = []
# declaram si initializam un dictionar gol
dict_gol = {}

# declaram si initializam un dictionar
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}
print(note_elevi)

# adaugare elemente
note_elevi['Sebi'] = 7
print(note_elevi)

# aflam nota lui Sebi
print(f'Nota lui Sebi este: {note_elevi["Sebi"]}')
print(f'Nota lui Sebi este: {note_elevi.get("Sebi")}')

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# dimensiunea dictionarului
print(f'Dimensiunea dictionarului: {len(note_elevi)}')

# stergem valori
note_elevi.pop("Gigel")
print(note_elevi.get("Gigel", 'Nu mai exista Gigel in dictionar'))
print(note_elevi)

print(f'Afiseaza doar cheile dictionarului: {note_elevi.keys()}')
print(f'Afiseaza doar valorile din dictionar: {note_elevi.values()}')