class Base1:
    def __init__(self):
        self.str1 = "Ayushi"
        print("Base 1 constructor called")

class Base2:
    def __init__(self):
        self.str2 = "Sharma"
        print("Base 2 constructor called")

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("derived class constructor called")

    def print(self):
        print(self.str1, self.str2)

d = Derived() #object is created, constrcutor is called
d.print()




