"""
Python supports file handling  i.e we can read and write files along with many other file
handling operations to operate on files.


Before performing any operation on the file like reading or writing, first we have to
open that file. For this, we can use inbuild function open()

Modes -
1. r : open an existing file for a read operation
2. w : open an existing file for a write operation, If the file has alreaady some content,
it will be overriden, but if the file is not created, then it will create a new file.
3. a : open an existing file for append operation. It will not override data.
4. r+  : To read and write data into file. Previous data will be overriden
5. w+ : To write and then read data. Previous data will be overriden.
6. a+ : To append and read data from file. It won't override existing data.

"""

# file = open('text1.txt', 'r')
# print(file.read())

# file = open('text1.txt', 'r')
# print(file.read(5))

# file = open('text1.txt', 'w')
# file.write("overrride data")
# file.close()

# file = open('text1.txt', 'r')
# print(file.read())

file = open('text2.txt', 'w')
file.write("new file")
file.close()
