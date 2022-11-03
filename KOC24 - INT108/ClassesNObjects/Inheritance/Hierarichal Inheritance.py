class Parent:
    def func1(self):
        print("this is function of parent class")

class Child1(Parent):
    def func2(self):
        print("this is function of child 1 class")

class Child2(Parent):
    def func3(self):
        print("this is function of child2 class")
        
c1 = Child1()
c1.func2()
c1.func1()

c2 = Child2()
c2.func3()
c2.func1()

