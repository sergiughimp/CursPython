class Patrat:
    '''
    Functia init = Constructorul clasei, de aici se construiesc obiecte
    '''
    def __init__(self, latura, culoare='alb'):
        self.latura = latura
        self.culoare = culoare

    def aria(self):
        return self.latura ** 2

new_patrat1 = Patrat(12)
print(f"Dimensiunea patrat 1 este: {new_patrat1.latura}")
print(f"Culoare patrat 1 este: {new_patrat1.culoare}")

new_patrat2 = Patrat(5, "rosu")
print(f"Dimensiunea patrat 2 este: {new_patrat2.latura}")
print(f"Culoare patrat 2 este: {new_patrat2.culoare}")


def aria(latura):
    return latura ** 2
'''
Metodele sunt doar functii pe obiecte (care primesc automat obiectul care le apeleaza ca si self - prin parametru
'''
print(aria(5))
print(f"Aria patratului 2 este: {new_patrat2.aria()}")
print(f"Aria patratului 1 este: {new_patrat1.aria()}")