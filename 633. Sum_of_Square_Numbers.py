# Jan 5 2020

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = int(c**0.5)
        for a in range(limit+1):
            res = (c - a**2)**0.5
            if int(res) == res:
                return True
        return False