#file connection
#read
myFile=open('sample.txt','r') #'r' evezine 'rt' yaza bilerik
data = myFile.read()

#write
myFile=open('sample.txt','a')
myFile.write("Salam")

myFile=open('sample.txt','w') #datani silir sonra yazir amma 'a'-da silmir
myFile.write("Salam")


import os
os.remove('test.txt') #fayli silir