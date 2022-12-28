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
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        s = set()
        
        while i < j:
            mine = nums[i]
            maxe = nums[j]
            avg = (mine + maxe)/2
            s.add(avg)
            i += 1
            j -= 1
        
        return len(s)
