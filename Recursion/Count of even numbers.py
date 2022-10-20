def countOfEvenNumbers(l):
    #1.base case
    if len(l) == 0:
        return 0

    y = countOfEvenNumbers(l[1:])  #count of even numbers from index 1  - 2.recursive call

    #3.small work
    if l[0] % 2 == 0:
        return 1 + y
    else:
        return y

l = list(map(int, input().split()))
count=countOfEvenNumbers(l)
print(count)
