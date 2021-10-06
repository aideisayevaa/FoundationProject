import json
from os import remove
with open('books.json','r') as f:
    data=json.load(f)


bookName = input("Kitabin adini daxil edin: ")


def findBookByName(bookName):
    i=0
    while i<100:
        for book in data["books"]:
            if book["title"]==bookName:
                print(book)
                break
            else:
                i+=1


pageNumberList=[]

def totalPaper():
    for book in data["books"]:
        pageNumberList.append(book["pages"])
    return(sum(pageNumberList))

    

countryName = input('Silmek istediyiniz olkenin adini daxil edin: ')
def deleteByCountry(countryName):
    # ölkə adı daxil edildiyi zaman o ölkəyə aid olan kitabların json faylından silinməsini təmin edin
    i=0
    while i<100:
        for book in data["books"]:
            if book["country"]==countryName:
                del book
                break
            else:
                i+=1
                

findBookByName(bookName)
print(totalPaper())
deleteByCountry(countryName)