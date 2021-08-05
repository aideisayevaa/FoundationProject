#evvelki derslerde readinge baxildi indi ise yazmaga baxilacaq
with open('data.txt','w') as myFile: #!!!! #eger data.txt faylimiz yox idise yeni sadece app.py variydisa ve bu kodu yazsaq onda ozu avtomatik olaraq data.txt faylini yaradir
    """ myFile.write("Star Wors I\n") """ #fayl yarandiqdan sonra bu yazini hemin fayl daxiline elave edir
    """ myFile.write("Star Wors II\n") """ #ikinciyi yazanda ise bosluq olmadan birincinin yaznindan yazildi

    #biz eger 3 ve 4cu setirdeki kodu silsek ve asagidaki kodu yazsaq guncellemis oluruq:
    """ myFile.write("Star Wors III") """

    #bunlari yazanda hamsisi yanyana yazilir bunun qarsisini almaq ucun \n yaziriq


#===============================================================

with open('data.txt','w') as my_file:
    """ my_file.write("Star Wors I\n") """
    """ my_file.seek(0)  """#bu funksiya vasitesile ilk 4 herfin yerine aida sozunu yazir yeni bu setirden sonraki kodlar 0dan baslayaraq yazilir
    """ my_file.write('aida') """
    print('Star Wors II',file=my_file) #12:07


with open('data.txt','a') as my_file:
    my_file.write('Star Wors I') #append ile evvelki silinmir yeni melumatlar evvelkinin uzerine elave edilir