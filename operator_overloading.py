# a = 2 + 3
# print(a)
# s = 'Mahak' + ' Pallavi'
# print(int.__add__(2, 3))

# print(s)
# print(str.__add__('Mahak', ' Pallavi'))

class Ranger:
    def __init__(self,name, eating, dancing):
        self.name = name
        self.eating_power = eating
        self.dancing_power = dancing

    def __add__(self, ranger2):
        self.eating_power = self.eating_power + ranger2.eating_power
        self.dancing_power = self.dancing_power + ranger2.dancing_power
        return self
    def __sub__(self, ranger2):
        self.eating_power = self.eating_power - ranger2.eating_power
        self.dancing_power = self.dancing_power - ranger2.dancing_power
        return self

    def display(self):
        print(f"{self.name}'s Eating power : {self.eating_power}")
        print(f"{self.name}'s Dancing power : {self.dancing_power}")

aryaman = Ranger('Aryaman', 23, 45)
rohan = Ranger('Rohan', 30, 45)

aryaman.display()
rohan.display()
# deepansh = aryaman + rohan
# aryaman.addpower(rohan)
# aryaman.display()
deepansh = aryaman + rohan
deepansh.name = 'Deepansh'
deepansh.display()

aryaman = Ranger('Aryaman', 23, 45)
rohan = Ranger('Rohan', 30, 45)

deepansh = aryaman - rohan
deepansh.name = 'Deepansh'
deepansh.display()