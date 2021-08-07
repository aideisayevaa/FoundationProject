with open('movies.txt','r') as myFile: #contect manager 
    """ print(myFile.read()) """ #falin oxunmasi zamani daha cox bu usuldan istifade olunur butunsetrleri oxuyur
    print(myFile.readline()) #yalnizca birinci setri oxuyur
    print(myFile.readline()) # ikinci defe yazanda ikinci setri oxuyur
    print(myFile.readline()) #bunlari yazanda bosluqlar olur olmamasi ucun print(myFile.readline(),end="") yaziriq


with open('movies.txt','r') as myFile:
    print(myFile.readlines(),end="") #tek setirde hamsini ekrana cixarir


#contect managerden istifade edende fayllari baglamaga ehtiyac qalmir

#biz eger 1 ve 2 ci setirden sonra print(myFile.read()) yazsaq onda error verir cunki fayl artiq baglanib
print(myFile.closed) #cavab true cixir cunki fayl baglanib




#===================================

#eger bizde 3 deyil daha cox setir olsa  print(myFile.readline()) bu kodu tekrar cox yazmaliyiq bunun qarsini almaq ucun fordan istifade edirik

with open('movies.txt','r') as my_file:
    for line in my_file:
        print(line)

    #bunun evezi olaraq :
    print(my_file.read()) 
    print(my_file.read(15)) #15 herfi(bosluq daxil) ekrana cixarir
