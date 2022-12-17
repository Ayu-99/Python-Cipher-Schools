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




