"""
Regular expressions - a regular expression is a special sequence of characters that uses a search pattern to find
a string or set of strings.

- It can detect the presence or absence of a text by matching it with a particular pattern.

- python provides re module that supports use of regex in python.

- Its primary function is to offer a search, where it takes a regular expression and a string. It returns
the first match or else none.

"""
#
# import re
# s = "This batch students doesn't respond and are sleeping students."
# match = re.search(r'students', s)
# print("start index: ", match.start())
# print("end index: ", match.end())


"""
Metacharacters- ., \, | , [], ^, ?, *, +
"""

# import re
# s = "This batch students.doesn't respond and are sleeping students."
# match = re.search(r'\.', s)
# print("start index: ", match.start())
# print("end index: ", match.end())

"""
^ - matches the beginning
"""
import re
s = "This batch students.doesn't respond and are sleeping students."
match = re.search(r'[^s]', s)
print("start index: ", match)

"""
$ - dollar (matches the end)
s$ - strings that ends with s like students, students
"""

"""
. - dot (matches one single character except for newline character)

[a.b.]

acby
adbi
ajbo

"""
"""
? - (question mark)
checks if string before the question mark in regex occurs at least once or not at all.

ab?c

ab
acb
dabc

"""

"""
* - star (matches zero or more occurences of regex preceeding the * symbol)

ab*c --- abc, abxyzc, 
"""


"""
[]- square bracket (specifies range of characters)
[0-3] [0123]
[a-c] [abc]
[^0-3] except 0,1,2,3
[^a-c] means any character except a,b,c
"""

import re
s = "This batch students.789 doesn't respond 123 and are sleeping students. 123"
regex = '\d+'
match = re.findall(regex, s)
print(match)


p = re.compile('[a-e]')  #p=[abcde]
s = "This batch students.789 doesn't respond 123 and are sleeping students. 123"
match = re.findall(p, s)
print(match)


