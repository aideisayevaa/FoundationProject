# __init__ double under metoddur
# print, len class ve s. evvelceden teyin olunan metoddur

class Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.Radius=radius

    def area(self):
        return self.Radius*self.Radius*self.pi

    def __repr__(self):
        return f'{__class__.__name__} nesnesi ve yaricapi {self.Radius}'

    def __len__(self):
        return self.Radius*self.Radius

circle_1=Circle(5)
print(circle_1)
print(circle_1.__repr__()) #bu iki kod eyni funksiyani yerine yetirir
print(dir(circle_1))#metodlari gosterir
print(int.__add__(4,8))

    