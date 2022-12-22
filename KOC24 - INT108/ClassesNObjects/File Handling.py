"""
FILE HANDLING

Python supports file handling i.e we can read and write files along with many other file
handling operations to operate on files.

---> Before performing any operation on the file like reading or writing, first we have to
open that file. For this we can use inbuild functions like open()

Modes-
1. r : open an existing file for a read operation.

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
