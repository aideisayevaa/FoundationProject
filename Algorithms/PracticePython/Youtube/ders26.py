#kecen dersde class insatnce veriables ile class verables arasindaki ferqden danisildi
#bu dersde: intance metodlar, class metodlar, statik metodlar

class Student:

    school_name = "X lisesi"
    number_of_students = 0 

    def __init__(self,name,age,grades):
        self.name = name 
        self.age = age 
        self.grades = grades
        Student.number_of_students +=1

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod #X lisesi sozundeki X-i deyismek ucun istifade olunur
    def display_school_name(cls, name_of_school): #self sozu kimi cls
        cls.school_name = name_of_school #cls self kimidi, school_name deyisir deye cls.shool_name yazdiq
         #class sozunun evezine cls yaziriq keyword olaraq cunki evvelceden class parametri qeyd olunub

    @staticmethod #statik metod herhansi bir deyisisklik etmir, classmetod ise deyisiklik edir 
    def statik(): #burada self, cls kimi parametrle7r yazilmir
        return "Sadece bu mesaji gonderiyor"


Student.display_school_name('Y Lisesi')

student_1=Student('Mahmut' , 33, [14,26,72,84])
student_2=Student('Fatma' , 33, [20,40,70,90])

print(Student.statik())
print(student_1.statik())
print(student_2.statik())


print(student_1.school_name)
student_1.school_name="Z lisesi" 

print(Student.school_name)
print(student_1.school_name)
print(student_2.school_name)


print(student_1.average())
print(student_2.average())


