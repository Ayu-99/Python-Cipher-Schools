""" rows = 3, cols = 3
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]

1. how to take matrix as input from user
2. display the matrix

"""
print("Enter number of rows: ")
rows = int(input())
print("Enter number of columns: ")
cols = int(input())
matrix = []
for i in range(rows):
    x = list(map(int, input().split()))
    #elements of a particular row (create row)
    # for j in range(cols):
    #     e = int(input())
    #     x.append(e)

    matrix.append(x)

print(matrix)
