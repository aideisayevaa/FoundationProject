""" import mymodule """ #as m_m #herdefe mymodule. ... yazmaq evezine m_m yazmaq ucun istifade olunur
""" import sys  
from mymodule import summation, mystring
numbers = [3,8,5,11]

sum = summation(numbers)

print(sum)
print(mystring)

print(sys.path) """ # var olan modullara baxir, yeni papkalari bir bir yoxlayir ilk once ders 31 faylina sonra zip faylina ve s.


# yuxarida yazilan kodlar fayllar eyni papkada olandaya aiddir

# eger mymodule faylini modules qovluguna yerlesdirsek 3cu setirde xeta cixir

from modules.test.mymodule import summation, mystring #bele yazdiqda modules qovlugundaki test qovlugundaki mymodule elcatimli oluruq cunki myprogram ile mymodule eyni seviyyede deyil

import math #hazir moduldan istifade etdik

print(math.pi)

import random
numbers=[3,6,7,9]
random_number=random.choice(numbers)
print(random_number)






