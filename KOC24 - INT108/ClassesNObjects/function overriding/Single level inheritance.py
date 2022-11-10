#function overrriding - ability of a child class to provide a specific implementation of a function that is
# already defined in its parent class.

"""
Inheritance--> inheriting properties from parent/base class to child/derived class
1. Single level
2. Multi level
3. Multiple
4. Hierarichal
5. Hybrid
"""
#Single level inheritance


class Parent:
    def __init__(self):
        self.value = "Inside parent"

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        self.value = "Inside child"

    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
obj1.show() #Inside Parent
obj2.show() #Inside Child

