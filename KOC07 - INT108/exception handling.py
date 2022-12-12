"""
there are 2 types of errors-
1. compile time - syntax error, indentation error
2. run time - exceptions


code1                 code2 (server-down)

"""
a=5
b=0
c=10
#try block, except block
try:
    print(c//a)
    print(a//b) #division is by 0 is invalid

except:
    print("runtime error occured")

 

#Multiple exceptions handling
a=5
b=0
c=10
#try block, except block
try:
    print(c//a)
    print(d)
    print(a//b) #division is by 0 is invalid


except ZeroDivisionError:
    print("runtime error occured")

except NameError:
    print("name error occured")
    
    
#raise an exception
a=5
b=0
c=10
#try block, except block
try:
    raise ZeroDivisionError
    # print(c//a)
    # print(d)
    # print(a//b) #division is by 0 is invalid


except ZeroDivisionError:
    print("runtime error occured")

except NameError:
    print("name error occured")

    
#finally block    
"""
Finally is always executed after try and except block. The final block always executes after normal termination
of try block or after try block terminates due to some exception.

"""
a=5
b=0
c=10
#try block, except block
try:
    raise ZeroDivisionError

finally:
    print("inside finally block")
