#  0 1 2 3 4
# l=[1,2,3,4,5]
# idx=0
# for item in l:
#     print(item, idx)
#     idx += 1

#enumerate -- is a function (predefined block of code which does some specific task)
#enumerate(iterable, start) 
#iterable (mandatory)-> any object that supports iteration
#start(optional)--> index value from which the counter is to be started, by default it is 0
# it adds a counter to iterable and return it in form of enumerating object.
l=["eat","sleep","code","sleep again","repeat"]
obj=enumerate(l,100)  #0 is by default
# print(type(obj))
# print(list(obj))

for idx, ele in obj:
    print(idx, ele)


# list
# tuple
# set
# dictionary
# string
