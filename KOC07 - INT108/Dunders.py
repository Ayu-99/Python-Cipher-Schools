"""
Dunder or magic methods/functions-
These are the methods having two prefix and suffix underscores in the method name.
For example: __init__, __len__

-- operator overloading

__init__ is used for initialization and is automatically called when object of the class is
created. Its like constructors in other languages like c++.
"""

class Demo:
    def __init__(self, string):
        print(string)

    def __demoDunder__(self, x):
        print(x*2)

s1 = Demo("ayushi")  #create object
s1.__demoDunder__(5)


