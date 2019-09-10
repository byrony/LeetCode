class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [i for i in range(1, n+1)]
        length = len(arr)-k
        return self.combine_(arr, k, length)
        
    def combine_(self, arr, k, length):
        res = []
        if k == 0:
        	# there is must return [[]], then later append [] to [item]
            return [[]]
        for i, item in enumerate(arr):
            for n in self.combine_(arr[i+1:], k-1, length):
                res.append([item] + n)
        return res