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





