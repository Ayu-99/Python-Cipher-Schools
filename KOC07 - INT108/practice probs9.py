"""
https://leetcode.com/problems/sort-the-people/

https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
"""

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for i in range(len(names)):
            l.append([heights[i], names[i]])
            
        l.sort(reverse=True)
        output=[]
        for i in l:
            output.append(i[1])
        return output   
            
        
