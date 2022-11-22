# s="this class*students*are way too boring"
# l=list(s.split())
# print(l)

"""
Join() function returns a string concatenated with the elements of iterable.

"""

l=["this", "class", "students", "are", "way", "tooo", "boring"]

s = "$".join(l)
print(s)

d={"this":1, "class students are":2, "boring":3}
print('_'.join(d))
