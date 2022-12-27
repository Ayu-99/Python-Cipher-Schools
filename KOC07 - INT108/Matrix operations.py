""" rows = 3, cols = 3
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]

1. how to take matrix as input from user
2. how to traverse in a matrix
3. how to find transpose of a matrix

"""

#1
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


#2
"""
     0  1  2 
[ 0 [1, 2, 3], 
  1 [4, 5, 6], 
  2 [7, 8, 9] ]

i=0,1,2
i = 0 , j = [0,1,2]
i=0 , j=0  matrix[0][0]
i=0 , j=1  matrix[0][1]
i=0 , j=2  matrix[0][2]

**********************
i=1 , j =[0,1,2]
i=1 j = 0 matrix[1][0]
"""
for i in range(0, rows):
    for j in range(0, cols):
        print(matrix[i][j])
        
#3
"""
[i][j]        [i][j]
[1][0]  --->  [0][1]

[1][2] --> [2][1]

                0  1  2 
original = [ 0 [1, 2, 3], 
           1 [4, 5, 6], 
           2 [7, 8, 9] ]
    
                  0   1  2
transposed = [ 0 [1  4  7]
             1 [2  5  8]
            2 [3  6  9]]  
"""

transpose = []
for i in range(rows):
    x = []
    for j in range(cols):
        x.append(0)
    transpose.append(x)

for i in range(rows):
    for j in range(cols):
        #  transpose[0][1]   matrix[1][0]
        transpose[j][i] = matrix[i][j]

print(transpose)       
