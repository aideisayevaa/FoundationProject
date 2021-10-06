#qeydiyyat ucun melumatlar: ad, soyad, email, password

users=[]
class User:
    def __init__(self,_ad, _soyad, _email, _password):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.password=_password
        users.append(self)

def getRegistrationData():
    ad=input("Ad: ")
    soyad=input("Soyad: ")
    email=input("Email: ")
    password=input("Password: ")
    return [ad,soyad,email,password]


def registerUser(lst):
    return User(lst[0],lst[1],lst[2],lst[3])

registerUser(getRegistrationData())
""" print(users) """

f = open('user.txt','w')
f.write(users[0].ad) #user.txt adli fayl yaradir ve users[0].ad deyerini yazdirir


f = open('user.txt','a')
for user in users:
    f.write(f'Name: {user.ad} | Surname: {user.soyad} | Email: {user.email} | Password: {user.password}')

    