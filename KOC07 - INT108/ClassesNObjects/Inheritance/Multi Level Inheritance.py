class GrandFather:
    def __init__(self, name):
        self.grandFatherName = name


class Father(GrandFather):
    def __init__(self, name, grandFatherName):
        self.fatherName = name
        GrandFather.__init__(self, grandFatherName)


class Daughter(Father):
    def __init__(self, name, fatherName, grandFatherName):
        self.daughterName = name
        Father.__init__(self, fatherName, grandFatherName)
        
    def print(self):
        print("Daughter name: " , self.daughterName)
        print("Father name: " , self.fatherName)
        print("Grandfather name: " , self.grandFatherName)

d1=Daughter("Joe", "Jim", "Jack")
d1.print()
