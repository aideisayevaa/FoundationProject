# fiziki olan her bir seyi 'nesne' deyirik nesnenin ozellikleri attribute, nesnelerin ede bildiyi funksiyalar metodlar var
#nesnelerin her birine mexsus xususiyyetler var
#bir sablon yaradiriq ve bir nece defe istifade edirik buna class deyilir


#######    Asagidaki kodlar optimal deyil cunki tekrarlanma var kodu optimallasdirmaq ucun 28ci setrdeki kod yazilir
""" class Car:
    pass #her hansi bir xeta verilmemesi ucun


car_1 = Car()
car_2 = Car()

car_1.brand = "BMW" #burada yazilan .brand atributlardir
car_1.model = "i5"
car_1.year = 2010

car_2.brand = "Audi" #burada yazilan .brand atributlardir
car_2.model = "x6"
car_2.year = 2012

print(car_1) #car nesnesinin yaddasdaki yeri gosterilir
print(car_1.brand)  """

""" 



class Car:
    #init ona gore istifade olunurki her yeni object yaradilanda onun xususiyyetlerini bir nece defe yazmayaq
    def __init__(self, brand, model, year): #self ona gore yazilir ki hemin anda yaradilan car nesnesinin branda aid olan xususiyyeti gostersin
        #init sozu initialize sozunden gotrulub. bu metodda atributlardan istifade edirik
        self.brand = brand #buradaki self sozunun evezine eslinde basqa soz de yazmaq olar 
        self.model = model
        self.year = year

    def brandmodel(self):
        return f'Araba markasi {self.brand} ve modeli {self.model} ' 

car_1 = Car('BMW', 'i5', 2010) #bunlar car_1 - e aid xususiyyetlerdir
car_2 = Car('Audi', 'x6', 2012)  #Car clasindan car_2 objecti yaradilir
#car_1 Car classinin instancesidir, yeni car_1 hem object hem de instancedir


print(car_1)
print(car_1.brand)

print(car_1.brandmodel())
 """



# name="Aida"
#message=f'salam {name}'
#print(message)

#message='salam {}'
#print(message.format(name))





class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def brandmodel(self):
        return f'Arabanin markasi {self.brand} ve modeli {self.model}'

car_1=Car("BMW","i5",2010)
car_2=Car("Audi","x6",2012)

print(car_1)
print(car_1.brand)
print(car_1.brandmodel())


class Movie:
    def __init__(self,name,director):
        self.name = name
        self.dircetor=director
    
    def movieName(self):
        return ("kinonun adi:" + self.name + " ve kinonun rejissoru:" + self.dircetor)

movie_1=Movie("name1","director1")
movie_2=Movie("name2","director2")

print("1ci kinonun adi: ", movie_1.name)
print("2ci kinonun adi: ", movie_2.name)
print("1ci kinonun rejissoru: ", movie_1.dircetor)
print("2ci kinonun rejissoru: ", movie_2.dircetor)

print(movie_1.movieName())




