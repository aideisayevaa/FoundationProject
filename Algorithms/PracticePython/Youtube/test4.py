class Istifadeci:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    @property
    def info(self):
        return f'{self.name} {self.surname}'


istifadeciler = []
while True:
    a=int(input("1-yeni telebe, 2-Aida"))
    if a==1:
        name=input("ad: ")
        surname=input("soyad: ")

        istifadechi=Istifadeci(name,surname)
        istifadeciler.append(istifadechi)

    for x in istifadeciler:
        print(x.info)