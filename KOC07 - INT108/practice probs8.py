"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

https://leetcode.com/problems/squares-of-a-sorted-array/

https://leetcode.com/problems/sorting-the-sentence/

https://leetcode.com/problems/check-if-the-sentence-is-pangram/

https://leetcode.com/problems/determine-if-string-halves-are-alike/


"""

#1
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maxCandies = max(candies)
        
        for i in range(len(candies)):
            if (extraCandies + candies[i]) >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        
        
        return result



#2
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            l.append(nums[i]**2)

        l.sort() 
        return l   

#3
class Solution:
    def sortSentence(self, s: str) -> str:
        current = list(s.split())
        output = [""]*len(current)

        for i in current:
            idx = int(i[len(i)-1])  #last value
            output[idx-1] = i[:len(i)-1]

        finalString = " ".join(output)
        return finalString 
      
 #4     
 class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(set(sentence)) == 26:
            return True

        else:
            return False   
          
#5
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        s1 = s[:len(s)//2]  #first half
        s2 = s[len(s)//2 :]  #second half
        
        vowelsInFirstHalf = 0
        vowelsInSecondHalf = 0
        
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s1:
            if i in l:
                vowelsInFirstHalf += 1
                
        for i in s2:
            if i in l:
                vowelsInSecondHalf += 1
                
        if vowelsInFirstHalf == vowelsInSecondHalf:
            return True
        
        return False
