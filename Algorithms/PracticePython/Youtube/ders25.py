""" name = 'Alakbar Taghiyev'
print(len(name))
print(name[0])
print(name.lower())
print(name.upper())
print(name.title())
print(name.find('b'))
print(name.count('a'))
print(dir(name))
print(help(str))
print(help(str.lower)) """



""" 
Student adinda bir class yaratmaq
properties(attributes) 3 adet name, age,grades //sinif
methos 1 eded grades (notlar) ortalamasini gosterir

init
self
instance nedir (nesne)
instance deyisenleri = instance properties

 """

class Student:

    school_name = "X lisesi"
    number_of_students = 0 #herbir instance yaradilanda sagirdlerin sayi artir

    def __init__(self,name,age,grades):
        self.name = name #buradaki name her bir studente gore ferqli olur
        self.age = age #bunlara instance aid propertiesler deyilir
        self.grades = grades
        Student.number_of_students +=1

    def average(self):
        return sum(self.grades) / len(self.grades) #burada sum() hazir funksiyadir

    def schoolName(self):
        return 'Okukumuzun adi'+ self.school_name


print(Student.number_of_students) #burada heleki instance yoxdur deye 0 cixir

student_1=Student('Mahmut' , 33, [14,26,72,84])#buradaki student_1 instance deyilir
student_2=Student('Fatma' , 33, [20,40,70,90])
student_3=Student('Fatma' , 33, [20,40,70,90])


print(Student.number_of_students)

""" print(student_1.average())
print(student_2.average())

print(student_1.name) """

student_1.name = "ahmet"  #adini deyisdirmek

""" print(student_1.name) """


#class veriables Class deyisenleri:

#Herbir instance veriables herbir nesneye gore deyise biler

#burada ortaq xususiyyetler de ola biler

#instanceler yeni nesneler ucun ortaq olacaq deyisenleri class deyisenleri olaraq yaza bilerik

""" print(student_1.school_name) """ #burada student_1 Studentr clasinin instancesidir ve school_name Studentin propertiesi(valuesidir)
""" print(Student.school_name) """ #clas adiylada cagirmaq olar

""" print(student_1.schoolName())
print(student_2.schoolName()) """

""" print(student_1.__dict__) """ #bu metod vasitesile nesnenin ve ya clasin sahib oldugu xususiyyetleri gosterir dictionary sozunden gotrulub
#bunu yazanda school_name cixmir cunki instanclara aid olan bir deyisen deyil student clasina aid deyisendir

""" print(Student.__dict__)  """#bunu yazanada gelir
