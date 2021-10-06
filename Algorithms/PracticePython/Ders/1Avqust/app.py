#istifadeciler qeydiyatdan kecir
#qeydiyatdan kecen istifadeciye rutbe veririk
#daxil olan istifadecinin rutbesine gore mesaj gosteririk

#yuxaridaki her bir emeliyyati ferqli fayllarda icra edirik
#yaritdigimiz fayllara modul deyeceyik

#yazdigimiz a ve b deyerlerini cagirmaq:
from user.register import b #bu sadece b ni import edir
from user.register import * #hamisini import edir, biz hamsini import etmekden ona gore hemise istifade etmirikki eyni adli deyisenler qarismasin
from user.register import b as firstB #eger her iki fayldan da b ni import edirikse onda qarismasinlar deye deyisene menimsedirik
from user.login import b as secondB


import user.register #hamisini import edir amma print edende ferqli cagrilir
import user.login #hamsini cagirir

import user

""" print(user.x) """

print(user.register.b)
print(user.login.b)




print(b)
