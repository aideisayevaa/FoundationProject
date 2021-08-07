""" 
C - Create Data`
R - Read Data
U - Update Data
D - Delete Data

"""



programMenusu=""" 
    ------Proqram menusu---------
    1-Yeni telebe elave et
    2-Telebelerin siyahisini gor
    3-Proqramdan cix
    4-Esas menyuya qayit
    """

# telebeAd,telebeSoyad,telebeYas
#proqram 3 hisseden ibaretdir: output,input ve onlar arasindaki alqoritmler
#telebeler=[] telebelerin hamsini saxlamaq ucun yaradilmis bir listdir
telebeler=[]
def telebeElaveEt():
    def yeniTelebe():
        ad=input("Ad: ")
        soyad=input("Soyad: ")
        yas=input('Yas: ')


        telebe={
            'Ad':ad,
            'Soyad':soyad,
            'Yas':yas
        }

        telebeler.append(telebe)

    while True:
        emr=input("Yeni telebe elave etmek isteyirsiniz? (Y/N) : ")
        if emr=='Y':
            yeniTelebe()
        else:
            break
    

def telebeSiyahisiniGor():
    for telebe in telebeler:
        print(f'{telebe["Ad"]}|{telebe["Soyad"]} | {telebe["Yas"]}')

def proqramdanCix():
    pass

def menuGoster():
    print(programMenusu)

menuGoster()
while True:
    emr=input('istediyiniz emeliyyatin nomresini daxil edin : ')
    if int(emr)==3:
        break
    elif int(emr)==1:
        telebeElaveEt()
    elif int(emr)==2:
        telebeSiyahisiniGor()
    elif int(emr)==4:
        menuGoster()
    else:
        print('Sehv emeliyyat nomresi daxil edildiyi ucun proqram dayandirilir')
        break


