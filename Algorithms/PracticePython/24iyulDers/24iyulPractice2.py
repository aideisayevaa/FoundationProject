""" class Corek:
    # constructor function- qurucu function
    def __init__(self,un,su,duz):
    # coreyin xususiyyetleri (statik)
       self.Un=un
       self.Su=su
       self.Duz=duz
    # behaviour- davranislar
    def CoreyiDogra(self):
        print('Corey dogranildi')


corek=Corek('BirmigdarUn','BirmigdarSu','BirmigdarDuz')
corek02=Corek(34,12,400)    
print(corek.Un,corek.Su)
corek.CoreyiDogra()
print(corek02.Un,corek02.Su)
corek02.CoreyiDogra() """



telebeSayi=0
while True:
    emr=input('Yeni telebe elave etmek isteyirsiniz? (Y/N): ')
    if emr=='Y':
        print('yeni telebe elave edildi')
        telebeSayi+=1

    else:
        print('Proqram yekunlasdi')
        print(telebeSayi)
        break
