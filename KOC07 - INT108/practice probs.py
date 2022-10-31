"""
Take 10 integer inputs from user and store them in a list.
Again ask user to give a number. Now, tell the user whether
that number is present in list or not. (Iterate over list
using while loop)
Take 20 integer inputs from user and print the following-
1. Number of positive numbers
2. Number of negative numbers
3. Number of odd numbers
4. Number of even numbers
5. Number of 0's
Take 10 integer inputs from user and store them in a list
Now, copy all the elements in another list but in
reverse order (Iterate using while loop)
Write a program to print sum, average of all numbers,
smallest and largest element of a list. (do not use inbuild max, min, avg, sum)
"""

#1
l=[]
for i in range(10):
    x= int(input())
    l.append(x)
x=int(input("enter a number"))
i=0
flag=False
while i < len(l):
    if l[i] == x:
        print("yes")
        flag=True
        break
    i+=1

if flag == False:
    print("no")
    
    
    
#2    
l=[]
for i in range(20):
    x= int(input())
    l.append(x)
    
countPositive=0
countNegative=0
countEven=0
countOdd=0
countO=0

for i in range(len(l)):
    if l[i] > 0:
        countPositive += 1
    
    if l[i] < 0:
        countNegative += 1
     
    if l[i] % 2==0:
        countEven+=1
    
    if l[i]%2 !=0:
        countOdd += 1
    
    if l[i] == 0:
        countO += 1

print(countOdd, countEven, countNegative, countPositive, countO) 



#3
l=[]
for i in range(10):
    x= int(input())
    l.append(x)
    
#[5,6,7,4,3]
#[3,4,7,6,5]
l1=[]
for i in range(len(l)-1, -1, -1):
    l1.append(l[i])
 
print(l1)


#4
l=[5,6,7,8,5,3,2,1]
sum=0
avg=0
max=float("-inf") #smallest floating number
min=float("inf") #largest floating

for i in range(len(l)):
    sum += l[i]
    if l[i] > max:
        max = l[i]
        
    if l[i] < min:
        min = l[i]
        
avg = sum/len(l)
print(sum, avg, max, min)
