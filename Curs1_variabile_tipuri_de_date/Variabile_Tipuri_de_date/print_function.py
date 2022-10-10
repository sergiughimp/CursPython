age = 25
first_name = "Adela"
last_name = "Neagu"

# print -> functie care 'scrie' in consola, dar care asteapta stringuri
print("My name is " + first_name + " " + last_name)
print("I am " + str(age) + " years old") # nu putem concatena age(int) cu str, deci trebuie sa facem type casting

# f-strings - formatted strings
print(f"My name is {first_name} {last_name} and I am {age} years old")

print(f"Afiseaza numele si prenumele in tupla {first_name, last_name}")

print(f"I grow up with one year, now I am {age + 1} years old!")

var_string = f"Here I will write more text... lore ipsum. Author: {first_name} {last_name}!"
var_string += f"I wrote more text!"
var_string += f"And all set!"
print(var_string)
