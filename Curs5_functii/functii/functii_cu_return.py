'''

return = valoarea returnata ==> Valoare pe care o functie o da inapoi la apelare

def func_name():
    ...
    cod
    ...
    return altceva

'''

# functia contor
# primeste o lista ca si parametri: o lista in care sa caute si elementul cautat
# returneaza: de cate ori apare elementul cautat in lista

def contor(lista, element_cautat):
    contor_element = 0
    for element in lista:
        if element == element_cautat:
            contor_element += 1
    print(f"Am terminat de cautat, am gasit ca {element_cautat} apare de {contor_element} ori in lista.")
    return contor_element
print(contor([1, 8, 6, 3, 2], 3))

''''
return este optional
dar putem avea si mai multe instructiuni de tip return, insa numai una dintre ele va fi activa la o apelare, deoarece atunci cand Python gaseste un return, opreste functia
'''

def functie_cu_multireturn(varsta):
    if varsta < 18:
        return "minor"
    elif varsta < 65:
        return "adult angajat"
    else:
        return "pensionar"

ionel = functie_cu_multireturn(54)
print(ionel)
maria = functie_cu_multireturn(12)
print(maria)