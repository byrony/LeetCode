# Jan 4 2020

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """            
        l, r = 1, n
        while l < r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l
        
            