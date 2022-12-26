"""
https://leetcode.com/problems/percentage-of-letter-in-string/

https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

***********************************

https://leetcode.com/problems/valid-anagram/

https://leetcode.com/problems/most-frequent-even-element/

"""

#1
class Solution:
    def percentageLetter(self, a: str, b: str) -> int:
        count=0
        for i in range(len(a)):
            if a[i]==b:
                count+=1
        zz=count/len(a)
        zzz=zz*100
        return (int(zzz))

#2
class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):

            if int(num.count(str(i)))!=int(num[i]):

                return False
                
        return True
      
      
#3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        return l1==l2
        

#4
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in d:
                    d[nums[i]] += 1
                else:
                    d[nums[i]] = 1
                    
        l = list(d.keys())
        l.sort()
        
        answer = -1
        maxCount = 0
        for i in l:
            maxCount = max(maxCount, d[i])
        
        for i in l:
            if d[i] == maxCount:
                return i
        
        return answer
