# Solution for 605. Can Place Flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_len = len(flowerbed)
        i = 0
        while i < flowerbed_len:
            if flowerbed[i] == 1:
                    i += 2
            else:
                # if left has space AND right has space
                #   the 1st                               i == the last 
                if (i == 0 or flowerbed[i - 1] == 0) and (i == flowerbed_len - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1 # planted
                    n -= 1
                    if n == 0: return True
                    i += 2
                else:
                     i += 1
        return n <= 0 # more secure, best practice
