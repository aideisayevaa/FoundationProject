""" with open('data2.txt','x') as my_file: #olamayan bir faylli yaratmaq ucun istifade olunur create emri, eger var olan bir fayli yazsaq error verir
    my_file.write('Python\n')
    my_file.write('Django\n')
    my_file.write('Java') """

#yuxariki kod error verdi cunki with open('data2.txt','x') as my_file: pass yazdiqdan sonra kodu run etdim ve fayl yaranda ikinci defe yazanda var olan fayla yazmis oldugumuz ucun error verdi


with open('data3.txt','x') as my_file:
    my_file.write('Python\n')
    my_file.write('Django\n')
    my_file.write('Java')

