# Jan 8 2020

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            allD = self.allDigits(n)
            for d in allD:
                if d == 0 or n % d != 0:
                    break
            else:
                res.append(n)
        return res
        
    def allDigits(self, n):
        res = set()
        while n//10 != 0:
            d, r = divmod(n, 10)
            res.add(r)
            n = d
        res.add(n)
        return res
        