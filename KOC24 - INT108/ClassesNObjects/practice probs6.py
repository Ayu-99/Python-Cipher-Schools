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
# 2 7 11 15   target=26
# a b    a
#   a      b
# time complexity: O(n*n)(max operations in worst case)
def sum(nums,target):
    for a in nums:
        for b in nums:
            s=a+b
            if s==target:
                if nums.index(a) != nums.index(b):
                    return [nums.index(a),nums.index(b)]
                else:
                    continue
            else:
                continue


#dictionary -- using extra space
d={}
"""
2 7 11 15 
d = {
 2 : 0,
 7 : 1,
 11: 2,
 15: 3
}
target = 26
each element in list
2 7 11 15
     ^
11 + x=26
x = 15    ---> return [3, 2]   11 and 15
"""

d={}
l=[2,7,11,15]
target = 26
for i in range(len(l)):
    d[l[i]] = i

for i in range(len(l)):
    x = target - l[i]
    if x in d:
        if d[x] != i:
            print([i, d[x]])
            break
            
# time complexity - O(n)  
# space complexity - O(n)
