"""
1. Create a class Student with two instance attributes student_name and student_marks. Create two member functions
a. print - to print the information of student (name and marks)
b. passOrFail - based on the marks, check whether student is pass or fail (pass if marks are greater than 33)


2. Create two derived class A and B inheriting from a base class C, then A class itself is base class for class D.

3. Create a class named Shape with function that prints "This is a shape"
Create another class named Polygon inheriting the Shape class with function that prints "Polygon is a shape"
Create two other classes Rectangle and Triangle inheriting from Polygon class having functions that say
"Rectangle is a polygon" and "Triangle is a polygon"

"""

#1
class Student:
    def __init__(self, name, marks):
        self.student_name = name
        self.student_marks = marks

    def print(self):
        print(self.student_name, self.student_marks)

    def passOrFail(self):
        if self.student_marks > 33:
            print("student is passed")
        else:
            print("student is failed")


s=Student("Ayushi", 25)
s.print()
s.passOrFail()




#2
class C:
    def __init__(self):
        print("Base Class C constructor called")

class A(C):
    def __init__(self):
        C.__init__(self)
        print("A derived class constructor called")

class B(C):
    def __init__(self):
        C.__init__(self)
        print("B derived class constructor called")

a=A()
b=B()


.#3
class Shape:
    def print1(self):
        print("This is a shape")

class Polygon(Shape):
    def print2(self):
        print("Polygon is a shape")

class Rectangle(Polygon):
    def print3(self):
        print("Rectangle is a Polygon")

class Triangle(Polygon):
    def print4(self):
        print("Triangle is a Polygon")

r=Rectangle()
r.print3()
r.print2()
r.print1()

t=Triangle()
t.print4()
t.print2()
t.print1()
