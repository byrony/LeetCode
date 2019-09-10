# first method exceeded time limit for the last test case
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A.sort()
        res = 0
        for i in range(len(A)-2):
            l = i+1
            r = len(A)-1
            while l < r:
                s = A[i] + A[l] + A[r]
                if s == target:
                    num_l = A[l]
                    num_r = A[r]
                    
                    #print(A[i], A[l], A[r], i, l, r)
                    multi_l = 1
                    # check duplicates
                    while l < r-1 and A[l]==A[l+1]:
                        l += 1
                        multi_l += 1
                    
                    multi_r = 1
                    while l < r-1 and A[r]==A[r-1]:
                        r -= 1
                        multi_r += 1
                    
                    #print(multi_l, multi_r)
                    if num_l == num_r:
                        res += (multi_l + multi_r) * (multi_l+multi_r-1) /2
                    elif num_l != num_r:
                        res += multi_l * multi_r
                    
                    l += 1
                    r -=1                                        
                    
                elif s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return res%(10**9+7)
        