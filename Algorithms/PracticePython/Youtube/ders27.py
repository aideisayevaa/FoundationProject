""" class Student:
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) 

student_1=Student('Mahmut' , 33, [14,26,72,84])
student_2=Student('Fatma' , 33, [20,40,70,90])

class UniverstyStudent(Student): #buradaki Student parent classdir
    pass #UniverstyStudent classi Sudent clasinin alt clasi sub child classidir
    #class UniverstyStudent(Student) bununla Student classinin xusuiyyetleri UniverstyStudent clasina da kecir


u_student_1 = UniverstyStudent('arin',22,[10,20,30])
print(u_student_1.age)
print(u_student_1.name)
print(u_student_1.average())

print(help(UniverstyStudent))

 """




""" ================================================================= """

class Student:


    test = "test student"

    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) 

student_1=Student('Mahmut' , 33, [14,26,72,84])
student_2=Student('Fatma' , 33, [20,40,70,90])

class UniverstyStudent(Student): 

    test = "Test Universty student"
    def __init__(self,name,age,grades,universty):
        super().__init__(name,age,grades) #parent classdan yeni student clasdan deyerleri alir   
        self.university = universty 


u_student_1=UniverstyStudent('arin',22,[10,20,30],"ITU")
#sub classin komekliyile parent classin deyerlerine elimiz catir amma tersi yox
print(u_student_1.university)
print(u_student_1.average())

print(Student.test)
print(UniverstyStudent.test)






class Student:



    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) 


class UniverstyStudent(Student):
    def __init__(self,name,age,grades,universty):
        super().__init__(name,age,grades)
        self.university=universty
student_1=Student('Mahmut' , 33, [14,26,72,84])
student_2=Student('Fatma' , 33, [20,40,70,90])

u_student_1=UniverstyStudent('Mahmut' , 33, [14,26,72,84],'DIA')
print(u_student_1.university)