"""
TASK:
Recursively find the count of 5 in the list

I/P
5 5 5 2 2 4 5 6 7

o/P
count of 5 is: 4
"""

def countOf5(l):
    if len(l) == 0:
        return 0

    y = countOf5(l[1:])  #3

    if l[0] == 5:
        return 1+y
    else:
        return y


l = list(map(int, input().split()))
count=countOf5(l)
print(count)



