# set =  structura de date care are doar elemente unice

set_gol = {} # dictionar
set_gol = set() # set
print(set_gol)

an = {'primavara', 'vara', 'toamna', 'iarna'}
print(an)

an.add('primavara')
print(an)

an.add('ceva')
print(an)

an.remove('vara')
print(an)

# Set membership
anotimp = "vara"
if anotimp in an:
    print("gasit")
else:
    print("nu exista in set")

print(f"Lungimea setului an {len(an)}")