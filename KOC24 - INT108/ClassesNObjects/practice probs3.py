"""
1. take a number as input from user in form of a string, calculate sum of cube of individual digits of that number
and then check whether the sum is equal to number itself or not.

2. take an integer input from user and print how many digits are there in that number.
"""

#1
n = input("Enter a number")
# "153" --->  "1" --> 1
sum = 0
for i in n:
    sum += int(i)**3

if sum ==  int(n):
    print("it is armstrong number")
else:
    print("its not armstrong number")

    
#2

    
    
    
