"""
ref: http://bookshadow.com/weblog/2016/09/11/leetcode-rotate-function/
"""


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        # this method is O(n^2)
        if len(A) == 0:
            return 0
        result = -float('inf')
        for i in range(0, -len(A), -1):
            F = 0
            k = i
            for j in range(0, len(A)):
                F += A[k] * j
                k += 1
            result = max(result, F)
        return result
        """

        size = len(A)
        sumn = sum(A)

        # compute the sum of F0
        F = 0
        k = 0
        for j in range(0, size):
            F += A[k] * j
            k += 1

        # compute the sum of F1, F2..., note F_next - F_previous = sum(A) - size * A[size - x], where x is the row index
        result = F
        for x in range(size - 1, 0, -1):
            F += sumn - size * A[x]  # use F_previous to compute F_next
            result = max(result, F)
        return result

