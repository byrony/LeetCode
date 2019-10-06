class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flower = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                new_flower += 1
            return new_flower >= n
        
        ## when len(flowerbed) >= 2
        i = 0
        while i < len(flowerbed):
            if i == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                new_flower += 1
                i += 2
            elif i == len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                new_flower += 1
                i += 2
            elif 0<i<len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                new_flower += 1
                i += 2
            else:
                i += 1
            if new_flower >= n:
                return True
            
        return False