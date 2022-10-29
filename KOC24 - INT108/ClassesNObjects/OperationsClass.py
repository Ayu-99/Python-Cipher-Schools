"""
Create a class Operations.
It should have four functions which performs, addition , subtraction, multiplication and division
on two values which are passed at time of object creation.

"""

class Operations:
    def __init__(self, a, b):
        self.first = a
        self.second = b

    def addition(self):
        print(self.first + self.second)

    def subtraction(self):
        print(self.first - self.second)

    def multiplication(self):
        print(self.first * self.second)

    def division(self):
        print(self.first // self.second)


o1 = Operations(5,6)  #address is in o1
print(o1)
o1.addition();
o1.subtraction();  # subtraction(o1)
o1.multiplication();
o1.division();
