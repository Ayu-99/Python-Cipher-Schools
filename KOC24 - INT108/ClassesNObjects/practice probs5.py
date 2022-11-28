"""
1. Write a Python class to reverse a string word by word.
Input string : 'hello .py world'
Expected Output : 'world .py hello'

2. Write a Python class which has two methods/functions get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
3. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

4. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
"""

#1
class ReverseClass:
    def reverseTheString(self, s):
        l = list(s.split(" "))
        l1 = l[::-1]
        s1 = " ".join(l1)
        return s1

r = ReverseClass()
finalString = r.reverseTheString("hello .py world")
print(finalString)


#2
class get_String:
    def get_string(self):
        self.str1=input()
    def print_string(self):
        print(self.str1.upper())
str1=get_String()
str1.get_string()
str1.print_string()


#3
class Rectangle:
    def Area(self,a,b):
        return a*b
    def Perimeter(self,a,b):
        return 2*(a+b)
a=2
b=3
r = Rectangle()
A=r.Area(a,b)
P=r.Perimeter(a,b)
print(A)
print(P)


#4
import math
class Circle:
    def Area(self,rad):
        return math.pi*rad*rad
    def Perimeter(self,rad):
        return 2*math.pi*rad
rad=int(input())
r = Circle()
A=r.Area(rad)
P=r.Perimeter(rad)
print(A)
print(P)







