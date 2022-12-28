"""
https://leetcode.com/problems/number-of-distinct-averages/

https://leetcode.com/problems/first-letter-to-appear-twice/
"""

#1


#2
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=[]
        for i in s:
            if i in l:
                return i
            else:
                l.append(i)
        
        return ""
