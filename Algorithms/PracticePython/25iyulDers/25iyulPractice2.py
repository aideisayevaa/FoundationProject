""" 
telebeler=[]


ad=input("Ad: ")
soyad=input("Soyad: ")
yas=input('Yas: ')

#bu 3 melumati bir yerde yigmaq lazimdi - dictionary

telebe={
    'Ad':ad,
    'Soyad':soyad,
    'Yas':yas
}

telebeler.append(telebe) #her yeni yaranan telebe telebeler adli liste elave edilir

print(telebe)
print(telebeler) """


#-----------------------------------------------------------



telebeler=[]


def telebeElaveEt():
    ad=input("Ad: ")
    soyad=input("Soyad: ")
    yas=input('Yas: ')


    telebe={
        'Ad':ad,
        'Soyad':soyad,
        'Yas':yas
    }

    telebeler.append(telebe)


def telebeSiyahisiniGoster():
    for telebe in telebeler:
        print(f'{telebe["Ad"]}|{telebe["Soyad"]} | {telebe["Yas"]}')

while True:
    emr=input("Yeni telebe elave etmek isteyirsiniz? (Y/N) : ")
    if emr=='Y':
        telebeElaveEt()
    else:
        telebeSiyahisiniGoster()
        break




