# @ bunlardan funksiyalari tek,imlesdirmek ucun istifade olunur
#@property olan metoda bir degisken kimi elcatimliliq olur

class Student:
    def __init__(self,name,surname,age,grades):
        self.name = name 
        self.surname = surname 
        self.age = age 
        self.grades = grades
        #self.fullname = self.name + ' ' + self.surname #fullname metod olaraq deyil property olaraqdi deye evvelki deyerleri oxuyur ona gore guncelenmis adi yox evveliki adi ekrana cixarir


    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    def average(self):
        return sum(self.grades)/len(self.grades)

student_1=Student('Aida','Isayeva',19,[10,20,30])

student_1.name = 'mahmut'
student_1.grades=[50,50,50] #ballari deyisdirdik



print(student_1.name)
print(student_1.surname)
print(student_1.fullname) #@property vasitesile fullname-i()-siz bele yazsaq metod olsa da property kimi elcatimliliq olur
print(student_1.average())

