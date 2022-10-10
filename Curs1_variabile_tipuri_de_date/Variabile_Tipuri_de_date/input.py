# input - functia cu care preluam date de la utilizator (tastatura)
# \n - newline, ducem cursorul pe urmatoare linie
name = input("Write the name: \n")
print(f"My name is {name}")

# by default, ce primim de la utilizator este string
age = input("How old are you? \n")
print(type(age))
age = int(age)
print(type(age))

# Exercitiu cu assert si input: cod CAPTCHA

x, y = 12, 13 # dam valori dinamice lui x si y, ca sa le putem schimba la fiecare rulare daca vrem
result_captcha = int(input(f"how much is {x} + {y}?\n"))
assert result_captcha == 25, "You are not a robot!"