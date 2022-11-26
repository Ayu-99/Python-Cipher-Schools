"""
1. Write a Python class to reverse a string word by word.
Input string : 'hello .py world'
Expected Output : 'world .py hello'

2. Write a Python class which has two methods/functions get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
3. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

4. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
"""

class ReverseClass:
    def reverseTheString(self, s):
        l = list(s.split(" "))
        l1 = l[::-1]
        s1 = " ".join(l1)
        return s1

r = ReverseClass()
finalString = r.reverseTheString("hello .py world")
print(finalString)
