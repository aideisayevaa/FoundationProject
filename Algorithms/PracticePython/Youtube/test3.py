""" ad=input("Adinizi daxil edin: ")
soyad=input("Soyadinizi daxil edin: ")
email=input("Emailinizi daxil edin: ") """
usarname=input("Usarname daxil edin: ")
password=input("Password daxil edin: ")

print('Hesabiniza daxil olun')
logInUsername=input('Username: ')
logInPassword=input('Password: ')

def yoxlamaUsername(usarname,logInUsername):
    if usarname==logInUsername:
        print("Melumatlar duzgundur")

    else:
        print("Yanlisdir")

def yoxlamaPassword(password,logInPassword):
    if password==logInPassword:
        print("Melumatlar duzgundur")

    else:
        print("Yanlisdir")
yoxlamaUsername(usarname,logInUsername)
yoxlamaPassword(password,logInPassword)

