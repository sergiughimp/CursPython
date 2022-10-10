class ContBancar:
    # constructorul
    def __init__(self, titularCont, iban):
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.active = False
        self.pin = 7777
        self.incercari_activare = 0

    def salut(self):
        print(f'Buna ziua: {self.titularCont}')

    def interogareSold(self):
        self.salut()
        print(f'Titularul {self.titularCont}')
        print(f'Iban {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.active}')
        print(f'Nr incercari {self.incercari_activare}')
        print(f'--------------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        self.pin_utilizator = pin_utilizator
        if pin_utilizator == self.pin:
            print(f'Card activat cu succes')
            self.active = False
        else:
            print(f'Pin gresit')
            self.incercari_activare += 1

    def alimentareCont(self, suma_depusa):
        self.salut()
        self.sold += suma_depusa
        print(f'Depunere cu succes, avem in cont suma de: {self.sold}')

    def plataCard(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'Ai cheltuit {suma_cheltuita}')
            print(f'Mai ai in cont {self.sold}')
        else:
            print(f'Fonduri insuficiente')