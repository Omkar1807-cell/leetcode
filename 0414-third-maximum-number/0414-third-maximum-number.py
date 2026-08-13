class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for i in nums:
            if i == largest or i == second or i == third:
                continue
            if i > largest:
                  third = second
                  second = largest
                  largest = i
            elif i > second:
                  third = second
                  second = i
            elif i > third:
                  third = i   
        if third == float('-inf'):
            return largest       

        return third       

        