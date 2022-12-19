"""
https://leetcode.com/problems/sum-of-unique-elements/

https://leetcode.com/problems/create-target-array-in-the-given-order/
"""

#1
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        
        sum = 0
        for i in list(d.keys()):
            if d[i] == 1:
                sum += i
        return sum        
        
