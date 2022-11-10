class Parent1:
    def show(self):
        print("inside parent1")

class Parent2:
    def display(self):
        print("inside parent2")

class Child(Parent1, Parent2):
    def show(self):
        print("inside child")

obj = Child()
obj.show() #inside child
obj.display() #inside parent2
