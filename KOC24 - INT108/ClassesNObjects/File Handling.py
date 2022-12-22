"""
FILE HANDLING

Python supports file handling i.e we can read and write files along with many other file
handling operations to operate on files.

---> Before performing any operation on the file like reading or writing, first we have to
open that file. For this we can use inbuild functions like open()


Modes-
1. r : open an existing file for a read operation.
2. w : open an existing file for a write operation. If the file has already some content,
it will get overriden. but if the file is not created, then it will create a new file.
3. a : open an existing file for append operation. It will not override existing data.
4. r+ : to read and then write data into file. Previous data will get overriden.
5. w+ : to write and then read data. Previous data will get overriden.
6. a+ : to append and read data from file. It won't override existing data.

"""

file = open('text1.txt', 'r')
print(file.read())

# file = open('text1.txt', 'r')
# print(file.read(10))

file = open('text2.txt', 'w')
file.write('new content of the file')

file = open('text1.txt', 'a')
file.write('| adding few more new content in the file')
file.close()

# with open('text1.txt') as f:
#     data = f.read()
# print(data)
#
# with open('text1.txt') as f:
#     f.write()

with open('text1.txt') as f:
    data = f.readlines()
    for line in data:
        word = line.split()
        print(word)


