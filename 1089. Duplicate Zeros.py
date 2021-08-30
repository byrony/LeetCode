# Aug 29, 2021
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0 
        while idx < len(arr):
            if arr[idx] == 0:
                j = idx + 1
                while j < len(arr) and arr[j] == 0:
                    j += 1
                
                dup_zero = j - idx
                arr[j:len(arr)] = ([0]*dup_zero + arr[j: len(arr)-dup_zero])[0:len(arr)-j]
                
                idx = j+dup_zero
                
            else:
                idx += 1
        return