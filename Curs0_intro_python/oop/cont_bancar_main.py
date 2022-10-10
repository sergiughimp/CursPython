from oop.cont_bancar import ContBancar

cont1 = ContBancar('Sergiu', 'RO9202')
cont2 = ContBancar('Marcela', 'DE03944')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(4444)
cont2.activareCont(7777)

cont1.alimentareCont(30)
cont2.alimentareCont(65)

cont1.plataCard(35)
cont2.plataCard(25)
cont2.plataCard(15)

cont1.interogareSold()
cont2.interogareSold()