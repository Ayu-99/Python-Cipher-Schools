# 1-10 - print even numbers

l1=[]
for i in range(1, 11):
    if i%2 == 0:
        l1.append(i)
print(l1)

#list comprehension
l = [i for i in range(1, 11) if i%2 == 0]
print(l)

"""
list comprehension consists of brackets containing the expression, which is executed for each element along with
the for loop to iterate over each element.

advantages?

"""

