if __name__ == '__main__':
    pass #birden cox python faylinin oldugu kodlarda bundan istifade edilir

print(__name__) #cavab olaraq __main__ cixir bu onu gosterirki app.py fayli birbasa icra olunur
#eger basqa bir fayldan import edilmis olsaydi onda impirt edilen faylin adi gosterilerdi

if __name__ == '__main__':
    print('test mesaji')