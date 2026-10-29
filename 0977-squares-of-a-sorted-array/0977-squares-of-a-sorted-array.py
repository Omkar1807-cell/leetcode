class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = []

        for num in nums:
            squares.append(num**2)

        return sorted(squares)
        