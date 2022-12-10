"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/

https://leetcode.com/problems/find-common-characters/

https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""

#1
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {} #words1
        d2 = {} #words2
        
        for i in words1:
            if i in d1:
                d1[i] += 1   #d1[i] = d1[i] + 1
            else:
                d1[i] = 1
        
        for i in words2:
            if i in d2:
                d2[i] += 1   #d2[i] = d2[i] + 1
            else:
                d2[i] = 1
        
        l = list(d1.keys())
        count = 0  #return 
        for i in l:
            if d1[i] == 1 and i in d2 and d2[i] == 1:
                count += 1
        
        return count
