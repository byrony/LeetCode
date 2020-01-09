# Jan 7 2020

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        for i in range(len(s)-1):
            j = i+1
            if s[i] == s[j]:
                return False
        return True