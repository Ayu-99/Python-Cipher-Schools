"""
#1
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.


#2
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

#3
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given a list of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

#4
Given a list of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.



"""

#1
s=input()
l=list(map(int,input().split(",")))
a=""
for i in range(len(s)):
    if i in l:
        a+=" "+s[i]
    else:
        a +=s[i]
print(a)


#2
l=[1,2,5,2,3]
target=2
l.sort()
output=[]
for i in range(len(l)):
    if l[i] == target:
        output.append(i)

print(output)


#4
l=[1,2,2,2,1,1,3]
d={}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

l=list(d.values())    #l=[3,3,1]
#set
s = set(l)   #s = {3,1}

if len(l) != len(s):
    print("false")
else:
    print("true")

