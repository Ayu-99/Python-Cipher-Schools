"""
1. given a list of numbers nums and an integer target, return the indices of two
numbers such that they add up to the target.

you may assume that each input would have exactly one solution, and you may not use the
same element twice.

you can return the answer in any order.

i/p
nums=[2,7,11,15]
target = 9

o/p=
[0,1]

"""
def func(x,t):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i] + x[j] == t:
                return i,j

l = [2,4,6,8]
r = 10
print(list(func(l,r)))
