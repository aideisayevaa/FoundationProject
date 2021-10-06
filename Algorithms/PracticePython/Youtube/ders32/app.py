#qovluqlarla isleyen zaman en vacib meselelerden birincisi o qovlugu, fayli acmaqdiq
myFile = open('movies.txt','r') #open yaziriq cunki fayli acmaq isteyirik sonra faylin adi yazilir, 'r' ona gore yazilir ki yalnizca oxumaq isteyirik deye
print(myFile.read()) #fayli oxuyur yeni butun yazilarini ekrana cixarir
print(myFile.name) #faylin adi ekrana cixir
print(myFile.mode) #faylin hansi mode-de olmasini gosterir, 'r' yazildigi ucun bu fayl read mode-dadir



myFile.close() #fayli baglamaq ucundur

print(myFile.closed) #faylin baglandigini yoxlamaq ucundur ekrana true ve ya false cixir

print(myFile.read()) #burada error cixir cunki fayli bağladiqdan sonra open funksiyasini yazana qeder read etmek olmur

#close() funksiyasi ona gore varki biz sadece 3 setirden ibaret olan txt fayllari ile deyil hemcinin daha cox setirli txt fayllari ile de isleyeceyik bu zaman onlari istifade etdikden sonra baglamasaq yaddasdan cox istifade eder