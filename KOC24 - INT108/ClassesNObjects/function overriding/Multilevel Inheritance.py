class Parent():
    def display(self):
        print("inside parent")

class Child(Parent):
    def show(self):
        print("inside child")
        
class GrandChild(Child):
    def show(self):
        print("inside grandchild")

g=GrandChild()
g.show()
g.display()
