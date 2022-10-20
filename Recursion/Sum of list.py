"""
Recursion - when a function calls itself
"""

def findSum(l):
    #base case
    if len(l) == 1:
        return l[0]

    return l[0]+findSum(l[1:]) #slicing in list - it will take list from 1 index


def findSum2(l):
    #base case
    if len(l) == 1:
        return l[0]

    return l[len(l) -1]+findSum2(l[:len(l)-1]) #slicing in list - it will take list from 1 index



l=[5,4,3,1,2]
s=findSum2(l)
print(s)


