class Student:
    def __init__(self, fname, fage):
        self.__name = fname
        self.age = fage
        self.__phoneno = '72429589809'

    def study(self):
        print(self.__name+ ' is studying')

    def dance(self):
        print(self.__name+ " is dancing!!")



pradeep = Student('Pradeep', 20)
pradeep.study()
pradeep.dance()
print(pradeep.__phoneno)
