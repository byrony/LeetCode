# Dec 19 2019

class Solution:
    def peakIndexInMountainArray(self, A):
        for i in range(len(A)-2):
            j = i + 1
            k = i + 2
            if A[j] > A[i] and A[j] > A[k]:
                return j