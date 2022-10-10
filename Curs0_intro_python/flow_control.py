# Flow control (if else) = controlam in functie de o conditie si bifurca codul in fuctie de rezultat

# if
print(f'Pornim radio')
piesa_faina = True
if piesa_faina == True:
    print('Dau mai tare Incep sa o fredonez')
print(f'Oprim radio')

# if ... else
# daca numarul este par printam acest lucru
# altfel printam impar

nr = 4
if nr % 2 == 0:
    print(f'numarul par este: {nr}')
else:
    print(f'numarul impar este: {nr}')

# verificam daca un numar este pozitiv
if nr > 0:
    print(f'numarul este pozitiv')
else:
    print(f'numatul este negativ')

# if else if else
# luam date de la tastatura si le transformam din string in int
ora = int(input('Introdu ora: '))
# print(f'Ora este: {ora}')
if ora < 0:
    print(f'ora nu exista')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print(f'buna ziua')
elif ora <= 21:
    print(f'buna seara')
elif ora <= 24:
    print(f'noapte buna')
else:
    print(f'ora nu exista')


# verificare drumuri viteza
viteza = int(input('Introdu viteza: '))
if viteza == 0:
    print(f'masina stationeaza')
elif viteza <= 50:
    print(f'masina merge prin localitate')
elif viteza <=90:
    print(f'masina merge pe drum judetean')
elif viteza <= 220:
    print(f'masina merge pe autostrada')
else:
    print(f'masina zboara')

# robotelul telefonic
optiunea = int(input('alege o optiune:'))
if optiunea == 0:
    print(f'meniu anterior')
elif optiunea == 1:
    print(f'ati ales romana')
elif optiunea == 2:
    print(f'ati ales engleza')
else:
    print(f'nu am indetificat optiunea, mai incearca')