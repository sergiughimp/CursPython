name = "Sergiu"
print(len(name))
print(name[2]) # va afisa al 3-lea caracter din string

# S e r g i u
# 0 1 2 3 4 5
print(name[1:3]) # va afisa er

# str[start: stop: pas] pas e in mod implicit 1
print(name[0: len(name): 2]) # sa afisa Sri
print(name[: len(name): 2])
print(name[0:: 2])
print(name[:: 2])
# cele 4 instructiuni de mai sus sunt echivalente, deoarece in sclicing putem omite capetele string-ului (sunt implicite)

# putem lucra cu valori negative la indexare/slicing
print(name[-1]) # name[len(name)-1] -> u
print(name[-2]) # i
print(name[-3]) # r

print("*" * 30)
print(name[::-1]) # sirul inversat

'''
Metode pe string
'''
s = "The coral is either the stupidest animal or the smartest rock.How are you?"
d = "1213"
print(d.isdigit())
print(s.isdigit())

first_sentence, second_sentence = s.split(".")
print(f"{first_sentence}.")
print(f"{second_sentence}")

print(f"the letter e appears {s.count('e')} times ")
print(f"the wold 'the' appears {s.count(' the ')} times")

print(s.index("a"))
print(s.upper())
print(s.lower())
print(s.replace("the", "***")) # va inlocui 'the' cu '***' in stringul s
print(s)

