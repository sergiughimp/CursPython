class Masina:
    culoare = "gri"
    viteza_actuala = 0
    culori_disponibile = {'verde', 'rosu', 'negru'}

    def __init__(self, marca, model, viteza_maxima, viteza_actuala, culoare, culori_disponibile, inmatriculata=False):
        self.marca = marca
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = viteza_actuala
        self.culoare = culoare
        self.culori_disponibile = culori_disponibile
        self.inmatriculata = inmatriculata
    def descriere_masina(self):
        for culoare in self.culori_disponibile:
            print(f"Culoarea masinei este {culoare}")
        # print(f"{self.marca} {self.model} {self.viteza_maxima} {self.viteza_actuala} {self.culoare}{self.culori_disponibile}{self.inmatriculata}")
        print("-"*80)
masina1 = Masina("Audi", "A4", 200, 0, "gri", {'verde', 'rosu', 'negru'})
print(masina1.descriere_masina())



