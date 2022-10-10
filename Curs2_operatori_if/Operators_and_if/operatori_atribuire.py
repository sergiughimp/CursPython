a = 10 # operatorul standart de atribuire
a += 2 # echivalent cu a = a + 2
a -= 2 # echivalent cu a = a - 2
a *= 2 # echivalent cu a = a * 2
a /= 2 # echivalent cu a = a / 2 -> aici a va deveni 10.0, deoarece impartirea normala da mereu un float
print(a)

a = int(a)
a //= 2 # operatorul // este pentru impartirea fara rest (impartirea intreaga)
print(a)

print(7 / 2)
print(7 // 2)