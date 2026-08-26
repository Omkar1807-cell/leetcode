class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = []
        maxLength = 0
        for char in s:
            while char in substring:
                substring.pop(0)
            substring.append(char)
            maxLength = max(maxLength,len(substring))
        return maxLength   


        