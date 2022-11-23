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

#if else
l=[]
for i in range(1,11):
    if i%2 == 0:
        l.append("it is even")
    else:
        l.append("it is odd")

print(l)

l1=["it is even" if i%2 ==0 else "it is odd" for i in range(1,11)]
print(l1)


"""
1. find all the numbers from 1-100 divisible by 8
2. find all the numbers from 1-100 that have 6 in them
3. count the number of spaces in a string
4. find all the words in the string which have less than 5 characters
"""

