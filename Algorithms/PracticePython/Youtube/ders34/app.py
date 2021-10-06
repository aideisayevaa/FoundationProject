#              1

with open('data.txt','r') as myFile:
    print(myFile.read()) #butun texti oxuyur
    print(myFile.read(5)) #eger 2ci setirden sonra bunu yazsaq 2ci  setirde hamsini oxudugu ucun  textin sonunda olur ve sondan 5 simvol oxumali oldugu ucun 5bosluq ekrana cixarir
    myFile.seek(6)
    print(myFile.read(5)) #6ciya qayidir ve 6dan sonraki 5 simvolu yazdirir
    print(myFile.read(4))
    print(myFile.tell()) #en son hansinda oldugunu bildirir



#              2
#courses listinin elementlerini bir fayla alt-alta yazmaq lazimdir
courses=['Python','Javascript','C++','Java','Ruby']
with open('data2.txt','w') as my_file:
    for elem in courses:
        print(my_file.write(elem+"\n"))



#              3
#movies.txt faylini oxuyub, her bir sirayi bir listde gosterek
with open('movies.txt','r') as my_File:
    file_content = my_File.readlines()
    """ print(file_content) """ #ekrana istediyimiz cavab cixsa bele \n-ler artiqdi her bir setir yeni setirde oldugu ucun avtomtik gelir onlar
    #\n - leri silmek isteyirirkse bele yaziriq:
    file_content=[ element.strip('\n')  for element in file_content if '\n' in element    ]
    print(file_content)  #14:50


#              4
#movies.txt faylini melumatlari ile birlikde kopyalamaq lazimdir
with open('movies.txt','r') as my_FIle:
    with open('movies2.txt','w') as my_FIle2:
        for line in my_FIle:
            my_FIle2.write(line)

