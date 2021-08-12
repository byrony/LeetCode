# 1368 ms
class Solution:
    def isSubsequence(self, s, t):
        dic = dict()
        for i, c in enumerate(t):
            if c not in dic:
                dic[c] = [i]
            else:
                dic[c].append(i)
        # print(dic)
        
        idx_init = -1
        for c in s:
            if c in dic.keys() and len(dic[c])>0:
                for i, idx in enumerate(dic[c]):
                    if idx > idx_init:
                        idx_init = idx
                        del dic[c][i]
                        break
                else:
                    return False
            else:
                return False
        return True


# 280 ms
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if t[j] != s[i]:
                j += 1
            else:
                i += 1
                j += 1
        
        if i == len(s):
            return True
        else:
            return False


# 252 ms
# with Binary Search wrote by Me. Note
class Solution:
    def isSubsequence(self, s, t):
        dic = dict()
        for i, c in enumerate(t):
            if c not in dic:
                dic[c] = [i]
            else:
                dic[c].append(i)
        # print(dic)
        
        idx_low_bound = -1
        for c in s:
            if c not in dic.keys():
                return False
            idx, _ = self.binaryInsert(dic[c], idx_low_bound)
            if idx < len(dic[c]) and dic[c][idx] > idx_low_bound:
                idx_low_bound = dic[c][idx]
            else:
                return False
        return True
    
    def binaryInsert(self, arr, n):
        # the binary search aglorith wrote by me is slower than build-in bisect_left. Also bisect_left return the first equal 
        # element index if it found one.
        """
        arr: a sorted arr
        n: a number need to insert into arr.
        return: index where to insert n. After the 1st number it met (e.g. if there are multiple it may met one in the middle firstly) which equals to n
        """
        l = 0
        r = len(arr)-1
        while l <= r:
            # print(l, r)
            mid = int((l+r)/2)
            if arr[mid] == n:
                return mid+1, mid+1
            elif arr[mid] > n:
                r = mid - 1
            else:
                l = mid + 1
        return l, r


# Apr 12, 2020
# solved with python string find method
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        for i in range(len(s)):
            idx = t[j:].find(s[i]) 
            # idx the index of first appearance, -1 if not found
            if idx == -1: 
                return False
            else:
                j += idx+1
        return True
                
                    

