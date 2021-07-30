""" ad='Hesen' """ #bu melumatlardan rahat istifade ede bilmek ucun bir qutuya yerlesdiririk
"""soyad='Memmedov'
yas=23 """
#lst=[ad,soyad,yas] #eyni xasseli olanlari yigmaq asandir

""" telebe01=['Hesen','Memmedov',23] """ #bunlar telebe1-in melumatlaridi amma deqiqlik yoxdu

#bunuhnla da yazmaq olar bu dictionarydi yeni key value istifade olunub
""" telebe01={ 
    'ad':'Hesen',
    'soyad':'Memmedov',
    'yas':23
} """

""" def eat():
    pass """ #metodun daxilinde heleki hecne yazmaq istemesek pass yaziriq bos metod yazmaq olmur deye

""" def showFullName():
    print(telebe01['ad']+" "+telebe01['soyad'])

showFullName() """

#bu void methoddur sadece icracidir ona verilen emrleri yerine yetirir istehsalci deyil
""" def Topla(a,b): """
    #a ve b ededlerini topla ve ekrana cap et
"""     print(a+b) """

#bu return methoddur mueyyen emrler de icra ede biler amma gorulen isin yaddasda saxlanilan bir neticesi olur, yaddasda saxlanilan bir mehsul istehsal edir
""" def Sum(a,b): """
    #a ve b ededlerini topla ve yaddasda saxla vaxt gelecek ondan istifade olunacaq
""" print("Hello") """ #returnden evvel yazildigi ucun bu emr icra olunur
""" return a+b
    print("Hello World") """ #return-den sonra yazilan print islemir cunki returnden sonraki emrler icra olunmur

""" Topla(3,5) """ #netice 8 alinir
""" Sum(3,5) """ #ekrana hec bir yazi cixmir, cunki return yazilib ve sadece deyer qaytarir print yazilmayib


""" c=Topla(3,5) """
""" print(c/2) """ #bele yazanda hec bir deyer istehsal olunmadigi ucun yeni printdir deye yalniz 3 ve 5i toplayir 8 alir amma bolme emeliyati yerine yetirmir
#bir sozle deyer istehsal olunmadigi ucun c/2 ifadesi NoneType olur
""" print(type(c)) """

""" c=Sum(3,5)
print(c/2) """ #bolme emeliyyatinin neticesi hemise float tipinde bir deyer verdiyi ucun 4.0 cavabi cixir
""" print(type(c)) """ #burada c-nin type-i int-dir


def Func(a,b):
    c=a+b
    return(c) #eger bunu yazmasaq c Func() daxilinden kenara cixa bilmir

def Func02(a,b):
    #Func methodunun icrasi neticesinde elde olunan deyerin tek ve ya cut oldugunu yoxlayin
    c=Func(a,b)
    if c%2==0:
        print('cutdur')
    else:
        print('tekdir')

Func02(3,4) #yazdigimiz kod iki metodun birbiriyle elaqelenmesini gosterir

#burada cemin tek ve ya cut olmasini bir funksiya daxikinde de yaza bilerdik amma single responsibilty-e gore toplamani ayri tek ve ya cut olmasini ayri tapdiq


class PizzaAparati:
    def __init__(self): #constructor function
        pass
        

    def KalbasaElaveEt(self,_kalbasa):
        self.kalbasa=_kalbasa #SELF-> PizzaAparati terefinden yaradilacaq pizzaya self adini ver

    def PendirElaveEt(self,_pendir):
        self.pendir=_pendir

pizza=PizzaAparati()
pizza.KalbasaElaveEt('1000Bereket')
pizza.PendirElaveEt('Westgold')


print(pizza.kalbasa)
print(pizza.pendir)

#void method
def Topla(a,b):
    print(a+b)

#return method
def Sum(a,b):
    return a+b

Topla(2,2)
c=Sum(1,2)
print(Sum(1,2))
""" c=Topla(3,5)
print(c/2) """
""" 
c=Sum(3,5)
print(c) """



