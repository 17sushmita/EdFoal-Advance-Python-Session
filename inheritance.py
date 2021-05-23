class Parent:
    def display(self):
        print("I'm the Parent")

class Parent2:
    def display2(self):
        print("I'm the Parent2")

class Child(Parent, Parent2):
    def display3(self):
        print("I'm the child")
child = Child()
child.display2()
child.display()
child.display3()