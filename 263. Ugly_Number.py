# Jan 4 2020

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        for n in [2,3,5]:
            while num%n == 0:
                num = int(num/n)
        return True if num == 1 else False