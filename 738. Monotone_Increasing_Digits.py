# Jan 31 2020

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digit = [int(i) for i in str(N)]
        
        i = len(digit)-1
        while i > 0:
            j = i-1
            if digit[i] < digit[j]:
                digit[i:] = [9]*(len(digit)-i)
                digit[j] -= 1
                i -= 1
            else:
                i -= 1
        # print(digit)
        return int(''.join([str(i) for i in digit]))