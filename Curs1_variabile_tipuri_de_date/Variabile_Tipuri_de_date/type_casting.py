# aceste 2 variabile sunt de tipul string
var1 = 42
var2 = "42"
var3 = "True"

print(type(var1))
print(type(var2))
print(type(var3))

# type casting - fortam conversia unei varibile de la un tip la altul
# var2 -> il convertim de la string la int (sau float)

my_int = int(var2)
# my_int este creat din valoarea pe care o aveam in var2, dar var2 nu se modifica si nici nu isi modifica tipul
print(var2, type(var2)) # 42 <class 'str'>
print(my_int, type(my_int)) # 42 <class 'int'>

var2 = int(var2) # modificare lui var2 prin suprascriere

# string -> bool
my_bool = bool(var3)
print(var3, type(var3))
print(my_bool, type(my_bool)) # True <class 'bool'>

var4 = "43"
my_float = float(var4)
print(var4, type(var4))
print(my_float, type(my_float)) # 43.0 <class 'float'>

# int -> float
another_float = float(my_int)
print(another_float, type(another_float))

# int -> bool
true = bool(5) # orice valoare diferita de 0 este considerata adevarata
false = bool(0)
print(true, type(true))
print(false, type(false)) #False <class 'bool'>

# Toate variabile se pot converti in string
my_string = str(another_float)
print(my_string, type(my_string)) # 42.0 <class 'str'>
