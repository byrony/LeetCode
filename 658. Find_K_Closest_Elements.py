# Sep 4 2021
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from bisect import bisect_left
        
        ins = bisect_left(arr, x)
        if ins == 0:
            return arr[:k]
        elif ins == len(arr):
            return arr[-k:]

        l, r = ins-1, ins
        left, right = [], []
        cnt = k
        while cnt > 0 and l >= 0 and r <= len(arr)-1:
            # if equal, prefer to add left element
            if abs(arr[l] - x) <= abs(arr[r] - x):
                left = [arr[l]] + left
                l -= 1
            else:
                right.append(arr[r])
                r += 1
            cnt -= 1
            # print(left, right, l, r, '===', cnt)
        
        if cnt > 0:
            if r >= len(arr):
                left = arr[l+1-cnt:l+1] + left
            elif l <= 0:
                right = right + arr[r:r+cnt]
        return left + right


# Dec 24 2019

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx_u, idx_l, idx_r = -1, -1, -1
        
        idx = self.binarySearch(arr, x)
        if len(idx) == 1:
            idx_u = idx[0]
        else:
            idx_l = min(idx)
            idx_r = max(idx)
        
        if idx_u == 0 or idx_r == 0:
            return arr[:k]
        if idx_u == len(arr)-1 or idx_l == len(arr)-1:
            return arr[-k:]
        
        # check the most closest K elements
        if len(idx) == 1:
            l = max(0, idx_u-k)
            r = min(len(arr)-1, idx_u+k)
        if len(idx) == 2:
            l = max(0, idx_l-k)   
            r = min(len(arr)-1, idx_r+k)
        
        diff = 0
        for i in range(l, len(arr)-k+1):
            new_last = arr[i+k-1]
            old_first = arr[i-1]
            if abs(new_last-x) < abs(old_first-x):
                diff += new_last - old_first
                res = arr[i:i+k]
            # print(i, diff)
        return res
        
    def binarySearch(self, arr, x):
        l = 0
        r = len(arr)-1
        while r >= l:
            mid = int((l+r)/2)
            if arr[mid] == x:
                return [mid]
            elif arr[mid] > x:
                r = mid-1
            elif arr[mid] < x:
                l = mid+1
        return [l, r]