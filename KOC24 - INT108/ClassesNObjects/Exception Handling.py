"""
Exception Handling -- v.v.v imp
try block
exception handling

there are two types of errors:
1. compile time error:  read about compile time error
2. run time error: divisionByZero, value error, key error

exception - run time error
"""


"""
data error
value error
syantax error
key error
ZeroDivisionError
"""


try :
    a = int(input())
    b = int(input())
    print(a//b)
    c=int(input())
    print(a//c)

except:
    print("error occurred")


    # Handling multiple exceptions

try :
    a = int(input())
    b = int(input())
    print(a//b)
    d={}
    print(d[5])

except ZeroDivisionError:
    print("error occurred")
    #different operations

except KeyError:
    print("key error occurred")
    

