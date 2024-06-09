class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max = max(candies)
        res = (i + extraCandies >= Max for i in candies)
        return res
