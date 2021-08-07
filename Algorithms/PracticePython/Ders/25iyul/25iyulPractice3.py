#C - Create Data
#R - Read Data
#U - Update Data
#D - Delete Data
programMenusu="""
    ----Proqram Menusu----
    1-Yeni Tələbə Əlavə Et
    2-Tələbələrin siyahısı gör
    3-Telebe sil
    4-Proqramdan cıx+9++
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
        print(f'{self.Id} nömrəli tələbə : {self.Ad} | {self.Soyad} | {self.Yas}')

id=1

def telebeElaveEt():

    def yeniTelebe():
        global id #***bu nedir?
        ad=input('Ad : ')
        soyad=input('Soyad : ')
        yas=int(input('Yas :'))

        Telebe(id,ad,soyad,yas)
        id+=1 #her telebe elave olunanda id 1 - 1 artir
    while True:
        emr=input('Yeni telebe elave etmek isteyirsiniz mi (Y/N) :')
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
    id=input("Silmek istediyiniz telebenin Id nomresini daxil edin :")
    for telebe in telebeler:
        if telebe.Id==int(id):
            telebeler.remove(telebe)
            break

def adFilteri():
    ad=input("Axtardiginiz telebenin adini daxil edin :")
    for telebe in telebeler:
        if telebe.Ad==ad:
            telebe.melumatlariGoster()   

def yasFilteri():
    yas=input("Minimal yas deyerini yazin :")
    for telebe in telebeler:
        if telebe.Yas>int(yas):
            telebe.melumatlariGoster()
            
menuGoster()
    
while True:
    
    emr=input('Istədiyiniz əməlyatın nömrəsini daxil edin :')
    if int(emr)==4:
        break
    elif int(emr)==1:
        telebeElaveEt()
    elif int(emr)==2:
        telebeSiyahisiGor()
    elif int(emr)==3:
        telebeSil()
    elif int(emr)==5:
        menuGoster()
    elif int(emr)==6:
        adFilteri()
    elif int(emr)==7:
        yasFilteri()
    else:
        print('Sehv emeliyyat nomresini daxil edildiyi ucun proqram dayandirilir')
        break
   
