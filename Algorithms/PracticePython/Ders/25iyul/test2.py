
programMenusu="""
    ----Proqram Menusu----
    1-Yeni Tələbə Əlavə Et
    2-Tələbələrin siyahısı gör
    3-Telebe sil
    4-Proqramdan cıx
    5-Əsas menuye qayit 
    6-Ad Filteri
    7-Yas Filteri
    ----------------------
    """ 
telebeler=[]
class Telebe:
    def __init__(self,_id,_ad,_soyad,_yas):
        self.Id=_id
        self.Ad=_ad
        self.Soyad=_soyad
        self.Yas=_yas
        telebeler.append(self)
    def melumatlariGoster(self):
        print(self.Id+" nomerli telebe"+self.Ad+" | "+self.Soyad+" | "+self.Yas)


id=1
def telebeElaveEt():
    def yeniTelebe():
        global id
        ad=input('Ad: ')
        soyad=input('Soyad: ')
        yas=int(input('Yas: '))

        Telebe(id,ad,soyad,yas)
        id+=1
    while True:
        emr=input("Yeni telebe elave etmek isteyirsiniz? (Y/N): ")
        if(emr=='Y'):
            yeniTelebe()
        else:
            break
def telebeSiyahisiGor():
    for telebe in telebeler:
        telebe.melumatlariGoster()

def menuGoster():
    print(programMenusu)

def telebeSil():
    id=input("Silmek istediyiniz telebenin id nomresinin daxil edin: ")
    for telebe in telebeler:
        if telebe.Id==int(id):
            telebeler.remove(telebe)
            break

def adFilteri():
    ad=input("Axtardiginiz telebenin adi: ")
    for telebe in telebeler:
        if telebe.Ad==ad:
            telebe.melumatlariGoster()

def yasFilteri():
    yas=input("Minimal yasi daxil edin: ")
    for telebe in telebeler:
        if telebe.Yas>int(yas):
            telebe.melumatlariGoster()

menuGoster()
while True:
    emr=input('Icra etmek istediyiniz emrin nomresini daxil edin: ')
    if int(emr)==4:
        break
    elif int(emr)==2:
        telebeSiyahisiGor()
    elif int(emr)==3:
        telebeSil()
    elif int(emr)==1:
        telebeElaveEt()
    elif int(emr)==5:
        menuGoster()
    elif int(emr)==6:
        adFilteri()
    elif int(emr)==7:
        yasFilteri()
    else:
        print('sehv emeliyyat nomresi')
        break
