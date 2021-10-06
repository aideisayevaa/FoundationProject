class Animal:
    varliq = 'canli'
    animal_count = 0
    def __init__(self,name,kind,color):
        self.name=name
        self.kind=kind
        self.color=color
        Animal.animal_count += 1

    def animalKind(self):
        return "pisiyin ayaqlarinin sayi " + self.kind

    @classmethod
    def varliqAdiDeyisme(cls,yeniVarliq):
        cls.varliq=yeniVarliq

    @staticmethod
    def statik():
        return "Bu pisiyin adi:"
    
cat=Animal("Tom","4 ayaqli","boz")
dog=Animal("Dog1","hsakdsk","qara")


Animal.varliqAdiDeyisme('cansiz')

print(Animal.varliq)
""" print(cat.varliq)
print(Animal.varliq)
print(Animal.animal_count)
print(cat.name)
print(cat.animalKind())
print(cat.__dict__) """

print(Animal.statik())


