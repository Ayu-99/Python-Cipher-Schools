"""
https://leetcode.com/problems/first-letter-to-appear-twice/

https://leetcode.com/problems/number-of-distinct-averages/
"""

#1
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=[]
        for i in s:
            if i in l:
                return i
            else:
                l.append(i)
                
        
        
 #2

