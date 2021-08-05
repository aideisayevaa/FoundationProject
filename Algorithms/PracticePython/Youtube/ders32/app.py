#qovluqlarla isleyen zaman en vacib meselelerden birincisi o qovlugu, fayli acmaqdiq
myFile = open('movies.txt','r') #open yaziriq cunki fayli acmaq isteyirik sonra faylin adi yazilir, 'r' ona gore yazilir ki yalnizca oxumaq isteyirik deye
print(myFile.read()) #fayli oxuyur yeni butun yazilarini ekrana cixarir
print(myFile.name) #faylin adi ekrana cixir
print(myFile.mode) #faylin hansi mode-de olmasini gosterir, 'r' yazildigi ucun bu fayl read mode-dadir
