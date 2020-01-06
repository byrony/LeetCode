# Jan 5 2020

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        from bisect import bisect
        
        arr = [int(i) for i in str(n)]
        i = len(arr) - 1
        while i > 0:
            j = i -1
            if arr[j] < arr[i]:
                # reorder arr[i:] to get the smallest greater number
                arr[i:] = sorted(arr[i:])
                swap_idx = bisect(arr[i:], arr[j]) 
                arr[j], arr[i+swap_idx] = arr[i+swap_idx], arr[j]
                break
            else:
                i -= 1
                j -= 1
        
        res = int(''.join([str(a) for a in arr]))
        if i == 0 or res > 2**31-1:
            return -1
        else:
            return res
        