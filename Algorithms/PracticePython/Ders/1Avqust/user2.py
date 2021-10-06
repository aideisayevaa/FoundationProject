import json


users=[]
class User:
    def __init__(self,_ad, _soyad, _email, _password):
        self.ad=_ad
        self.soyad=_soyad
        self.email=_email
        self.password=_password
        users.append(dict(self)) #obyekti json faylina cevirmek olmur deye dictionarye kecib ele jsona keciririk

def getRegistrationData():
    ad=input("Ad: ")
    soyad=input("Soyad: ")
    email=input("Email: ")
    password=input("Password: ")
    return [ad,soyad,email,password]


def registerUser(lst):
    user =  User(lst[0],lst[1],lst[2],lst[3])
    users.append(user.__dict__)


userData = getRegistrationData()
registerUser(userData)


f = open('user.json','w')

jData=json.dumps(users) #bizde olan datani json formatina kecirmeliyik

f.write(jData)
    