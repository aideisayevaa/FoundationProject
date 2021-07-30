menu=""" 
Qeydiyyatdan keçmək üçün 1 daxil edin
Sistemə daxil olmaq üçün 2 daxil edin
 """
istifadeciler=[]
class Istifadeci:
    def __init__(self,ad,soyad,email,username,password):
        self.Ad=ad
        self.Soyad=soyad
        self.Email=email
        self.Username=username
        self.Password=password
        istifadeciler.append(self)
    def melumatlariGoster(self):
        print(self.Ad+" "+self.Soyad+" "+self.Email+" "+self.Username+" "+self.Password)
        
def melumatlarGoster():
    for istifadeci in istifadeciler:
        istifadeci.melumatlariGoster()

def qeydiyyatdanKec():
    def yeniIstifadeci():
        ad=input("Ad: ")
        soyad=input("Soyad: ")
        email=input("Email: ")
        username=input("Username: ")
        password=input("Password: ")
        Istifadeci(ad,soyad,email,username,password)

    while True:
        emr=input("Yeni istifadeci daxil etmek isteyirsinizmi? (Y/N): ")
        if emr=='Y':
            yeniIstifadeci()
        else:
            break


def daxilOl():
    username=input("Username: ")
    password=input("Password: ")
    for istifadechi in istifadeciler:
        if istifadechi.Username==username and istifadechi.Password==password:
           melumatlarGoster()
        else:
            emr=input("Daxil etdiyiniz məlumatları yoxlayın ya da qeydiyyatdan keçmək üçün Q hərfinə basın: ")
            if emr=='Q':
                qeydiyyatdanKec()
            else:
                print('Daxil olunan melumat yanlisdir')


def menuGoster():
    print(menu)

menuGoster()

while True:
    emr=input("Nomre daxil edin: ")
    if int(emr)==1:
        qeydiyyatdanKec()
    elif int(emr)==2:
        daxilOl()
    else:
        print('Sehf nomre daxil edildi')
        break