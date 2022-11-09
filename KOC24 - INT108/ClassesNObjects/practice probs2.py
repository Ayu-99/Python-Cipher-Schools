"""
Create a class Calculate
it should have 3 functions-
1. to find the modulus of two numbers (two numbers should be instance variables)
2. to find the power (x**y --> take x and y as argument)
3. to find the average(it should take list as argument)
Create object of class and perform these 3 functions
"""
class Calculate:
    def __init__(self, x,y):
        self.first = x
        self.second = y

    def modulus(self):
        print(self.first % self.second)

    def power(self, x, y):
        print(x**y)

    def average(self, l):
        s = sum(l)
        print(s/len(l))

x=int(input("input x:"))
y=int(input("input y:"))
o1= Calculate(x,y)
o1.modulus();
o1.average([1,2,3,4,5])
o1.power(2,4);
