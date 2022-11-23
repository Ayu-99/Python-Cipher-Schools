l=[]
for i in range(1,11):
    if i%2 ==0 :
        l.append(i)
print(l)

#list comprehension
l = [i for i in range(1,11) if i%2 == 0]
print(l)

"""
list comprehension consists of brackets containing the expression which is executed for each element along 
with the for loop to iterate over each element in the list.

Adv-
1. less lines of code - space efficient
2. it provides short syntax for creating a new list

"""

s="abcdefghi"
l=[]
for i in s:
    l.append(i)
print(l)

l1=[i for i in s]
print(l1)


#nested list comprehension
l=[]
for i in range(1,4):
    for j in range(1,3):
        l.append((i,j))
print(l)

l1=[(i,j) for j in range(1,3) for i in range(1,4)]
print(l1)


