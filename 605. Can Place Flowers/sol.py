class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    count += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        return count >= n
