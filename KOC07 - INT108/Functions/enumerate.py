#  0 1 2 3 4
# l=[1,2,3,4,5]
# idx=0
# for item in l:
#     print(item, idx)
#     idx += 1
#

#enumerate ---> function  predefined block of code

# enumerate() -> keeps a counter of an iterable and returns it in form of enumerating object.

# list
# tuple
# set
# dictionary
# string

l=[1,2,3,4,5]

obj=enumerate(l,3)  #0 it takes by default
# print(type(obj))
print(list(obj))
"""
o/p
ele idx
"""
