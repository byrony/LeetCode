# Dec 21 2019

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= (n-1)
            cnt += 1
        return cnt
        