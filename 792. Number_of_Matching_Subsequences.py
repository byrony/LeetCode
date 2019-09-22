class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        dic = dict()
        for i, c in enumerate(S):
            if c not in dic:
                dic[c] = [i]
            else:
                dic[c].append(i)
        # print(dic)
        res = 0
        for w in words:
            if self.isSubsequence(w, dic):
                res += 1
        return res
    
    def isSubsequence(self, s, dic):
        idx_low_bound = -1
        for c in s:
            if c not in dic.keys():
                return False
            # idx = self.binaryInsert_(dic[c], idx_low_bound)
            # if idx < len(dic[c]) and dic[c][idx] > idx_low_bound:
            #     idx_low_bound = dic[c][idx] 
            # or 
            idx = self.binaryInsert(dic[c], idx_low_bound)
            if idx < len(dic[c]) and dic[c][idx] >= idx_low_bound:
                idx_low_bound = dic[c][idx] + 1
            else:
                return False
        return True
    
    def binaryInsert(self, arr, n):
        from bisect import bisect_left
        return bisect_left(arr, n)
    
    def binaryInsert_(self, arr, n):
        # the binary search aglorith wrote by me is slower than build-in bisect_left, cannot pass last test case
        """
        arr: a sorted arr
        n: a number need to insert into arr.
        return: index where to insert n. After the 1st number it met which equals to n
        """
        l = 0
        r = len(arr)-1
        while l <= r:
            # print(l, r)
            mid = int((l+r)/2)
            if arr[mid] == n:
                return mid+1
            elif arr[mid] > n:
                r = mid - 1
            else:
                l = mid + 1
        return l