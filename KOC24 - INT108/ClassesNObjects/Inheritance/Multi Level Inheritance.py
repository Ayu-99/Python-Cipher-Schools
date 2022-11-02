class GrandFather:
    def __init__(self, name):
        self.grandFatherName = name

class Father(GrandFather):
    def __init__(self, name, grandFatherName):
        GrandFather.__init__(self, grandFatherName)
        self.fatherName = name

class Daughter(Father):
    def __init__(self, name, fatherName, grandFatherName):
        Father.__init__(self, fatherName, grandFatherName)
        self.daughterName = name
        
    def print(self):
        print("Daughter name: ", self.daughterName)
        print("Father name: ", self.fatherName)
        print("GrandFather name: ", self.grandFatherName)

d1= Daughter("Joe", "Jim", "Jack")
d1.print()
