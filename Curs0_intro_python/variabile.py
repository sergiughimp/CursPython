# variabila = zona de memorie din calculator care tine date
# variabile = cutie in care punem valori


# am declarat si initializat variablia marca
marca_masina = 'Volvo'
# am declarat si initializat variablia model
model_masina = 'XC 60'

# nu putem pune spatiu in numele variabilei
# o variabila incepe cu o litera mica
print(marca_masina, model_masina)
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# suprascriere
model_masina = 'XC 60 Face Lift'
print(f'Modelul nou al masinei este: {model_masina}')

# loosely typed = nu specificam tipurile ex: Python
# strongly typed = specificam tipurile ex: Java


nume = 'Ghimp'
prenume = 'Sergiu'
varsta = 26
print(nume + ' ' + prenume)
print(f'{nume} {prenume} are varsta de {varsta}')


a = 3
b = 3
print(a + b)
a = '3'
b = '3'
print(a + b)