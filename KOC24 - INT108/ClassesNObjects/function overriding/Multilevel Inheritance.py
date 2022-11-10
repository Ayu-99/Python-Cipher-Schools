#Multilevel

class Parent():
    def display(self):
        print("inside parent")

class Child(Parent):
    def show(self):
        print("inside child")

class GrandChild(Child):
    def show(self):
        # Child.show(self)
        super().show() #call the function in parent class
        print("inside grandchild")

g=GrandChild()
g.show()
g.display()


