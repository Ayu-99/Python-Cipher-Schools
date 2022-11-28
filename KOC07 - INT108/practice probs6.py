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
r = 14
print(list(func(l,r)))

"""
using dictionary
[2 4 6 8]   [2, 3]
 ^ ^ ^
d={
 2 : 0,
 4 : 1,
 6 : 2,
 8 : 3
}

target = 14
x + y = target
    x  =   14 - 6 = 8

"""

l=[2,4,6,8]
target=10
d={}
for i in range(len(l)):
    d[l[i]] = i

for i in range(len(l)):
    x = target - l[i]
    if x in d and i!=d[x]:
        print([i, d[x]])
        break
        
# time complexity-O(n)   
# space complexity- O(n) 
