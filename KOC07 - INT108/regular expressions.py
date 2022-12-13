"""
Regular expressions - a regular expression is a special sequence of characters that uses a search pattern to find
a string or set of strings.

- It can detect the presence or absence of a text by matching it with a particular pattern.

- python provides re module that supports use of regex in python.

- Its primary function is to offer a search, where it takes a regular expression and a string. It returns
the first match or else none.

"""

import re
s = "This batch students doesn't respond and are sleeping students."
match = re.search(r'students', s)
print("start index: ", match.start())
print("end index: ", match.end())
