"""
Regular expressions - wide topic (basics)
Regular expressions is a special sequence of characters that uses a search pattern to find
a string or set of strings.
"""
import re
s = "This batch students doesn't respond and are sleeping students."
match = re.search(r'students', s)  #first occurence it will give
print("start index: ", match.start())
print("end index: ", match.end())


"""
Meta characters - Regular expressions
., \, |, [], ^, ?, *, +

"""

import re
s = "This batch doesn't respond and are sleeping."
try:
    match = re.search(r'\.', s)  #first occurence it will give
    print("start index: ", match.start())
    print("end index: ", match.end())
except AttributeError:
    print("error occurred")

"""
^ --> matches the beginning
"""
import re
s = "the students are not listening."
try:
    match = re.findall('^t', s)  #first occurence it will give
    if match:
        print("yes, string starts with s")
    else:
        print("does not start with s")
except AttributeError:
    print("error occurred")
    
"""
$ - matching the end
"""

"""
. --> matches one single character except for newline character
* --> matches with multiple characters
"""
import re
s = "the students ae not listening"
try:
    match = re.findall('a*e', s)  #first occurence it will give
    print(match)
    if match:
        print("found the occurrence")
    else:
        print("did not find")
except AttributeError:
    print("error occurred")


"""
? --> zero or more occurences
"""

# import re
# s = "the students ae not listening"
# try:
#     match = re.findall('a?e', s)  #first occurence it will give
#     if match:
#         print("found the occurrence")
#     else:
#         print("did not find")
# except AttributeError:
#     print("error occurred")

"""
[]  --> set of characters
"""
# import re
# s = "the students are not listening"
# try:
#     match = re.findall('[a-d]', s)  #first occurence it will give
#     if match:
#         print(match)
#     else:
#         print("did not find")
# except AttributeError:
#     print("error occurred")

    
