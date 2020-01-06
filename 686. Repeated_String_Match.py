# Jan 5 2020

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        rep = int(len(B)/len(A)) + 2
        i = rep-2
        A_rep = A*i
        while i <= rep:
            if B in A_rep:
                return i
            else:
                i += 1
                A_rep += A
        return -1