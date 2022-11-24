"""
#1
You will be given multiple substrings, and you have to concatenate them using $

i/p
"hi" "hello" "how u doing" "nice weather"

o/p
"hi$hello$how u doing$nice weather"


#2
create a python class Birthday that takes two variables-
1. a string called name
2. a string called age

do not forget init function

create a member function that increases the value of age by 1
create an instance/object of class and age should be 23 and name should be "Jack" for
that object. call the age method to increase age of Jack and then print the age of
Jack.

#3
you have a list of characters. you have to print count of each character in list
take character list input from user

i/p
7
a
b
c
a
b
c
c

o/p
a : 2
b : 2
c : 3

"""

#1
n=int(input("How many substrings you want to give:"))
l=[]
for i in range(0,n):
    a=input()
    l.append(a)
print('$'.join(l))


#2
class Birthday:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def incrementAge(self):
        return self.age + 1

s=Birthday("Jack", 23)
print(s.incrementAge())

#3
use dictionary to keep the count of each character
key == character
value == count of each character
