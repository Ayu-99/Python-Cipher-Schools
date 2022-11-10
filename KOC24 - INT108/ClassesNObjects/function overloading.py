#write a function to multiply two numbers

def multiply(a, b):
    return a*b

def multiply(a,b,c):
    return a*b*c

#default values always give from right to left
def multiply(*argv):
    for parameter in argv:
        print(parameter)

y = multiply("hello", 5, "hi", 6.7, 'a')
z = multiply(4,5,6,6,7)
print(y)

#function overloading - name of the function is same but difference can be in number of parameters and data type
# of parameters

#function overloading is not supported, the function taken will be  the latest defined function

"""
Functions
different types of arguments????
1. default arguments
2. keyword arguments
3. variable length arguments

"""
