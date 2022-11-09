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

l=["eat","sleep","code","dance","sleep again"]

obj=enumerate(l, 0)  #0 it takes by default
# print(type(obj))
# print(list(obj))

for idx, ele in obj:
    print(idx, ele)

"""
o/p
ele idx
"""
