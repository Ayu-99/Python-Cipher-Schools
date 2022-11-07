PRACTICE:

1. Create a class Student with two instance attributes student_name and student_marks. Create two member functions
a. print - to print the information of student (name and marks)
b. passOrFail - based on the marks, check whether student is pass or fail (pass if marks are greater than 33)

2. Create two derived class A and B inheriting from a base class C, then A class itself is base class for class D.

3. Create a class named Shape with function that prints "This is a shape"
Create another class named Polygon inheriting the Shape class with function that prints "Polygon is a shape"
Create two other classes Rectangle and Triangle inheriting from Polygon class having functions that say
"Rectangle is a polygon" and "Triangle is a polygon"


#1
class Student:
    def __init__(self, name, marks):
        self.student_name=name
        self.student_marks=marks

    def print(self):
        print(self.student_marks)
        print(self.student_name)

    def passOrFail(self):
        if (self.student_marks > 33) :
            print("student is passed")

        else:
            print("student is failed")

s=Student("Ayushi",30)
s.print()
s.passOrFail()
