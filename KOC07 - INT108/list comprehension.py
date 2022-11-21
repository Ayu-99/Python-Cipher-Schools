# 1-10 - print even numbers

# l1=[]
# for i in range(1, 11):
#     if i%2 == 0:
#         l1.append(i)
# print(l1)
#
# #list comprehension
# l = [i for i in range(1, 11) if i%2 == 0]
# print(l)

"""
list comprehension consists of brackets containing the expression, which is executed for each element along with
the for loop to iterate over each element.

advantages?
1. space efficient, it requires fewer lines of code
2. time efficient
"""

# for i in range(1,20):
#     print(i)
#
# l=[i for i in range(1,20)]
# print(l)

l=[]
s="today is good day"
for c in s:
    l.append(c)
print(l)

l1 = [c for c in "today is good day"]
print(l1)


"""
1. find all the numbers from 1-100 divisible by 8
2. find all the numbers from 1-100 that have 6 in them
3. count the number of spaces in a string
4. find all the words in the string which have less than 5 characters
"""
#1
mylist = [x for x in range(1, 101) if x % 8 == 0]
print(mylist)

#2
l = [i for i in range(1,101) if "6" in str(i)]
print(l)

#3
A= 'aa bb cc ff '
B = [c for c in A if c == ' ']
print(len(B))

#4
strng2 = "My name is kunal"
print([i for i in strng2.split() if len(i) < 5])

"""
nested list comprehension

nested loops
"""
# for i in range(1,5):
#     for j in range(1,4):
#         print(i, j)

# l=[[j for j in range(1,4)] for i in range(1,5)]
# print(l)


numbers=[i*10 for i in range(1,6)]
print(numbers)

# map, lambda
numbers1= list(map(lambda i: i*10, [i for i in range(1,6)]))
print(numbers1)

#if else in list comprehension
l=[]
for i in range(1,6):
    if i%2 ==0:
        l.append("it is even")
    else:
        l.append("it is odd")

print(l)

l1= ["it is even" if i%2 == 0 else "it is odd" for i in range(1,6)]
print(l1)

