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
