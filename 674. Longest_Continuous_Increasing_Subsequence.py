# Dec 17 2019

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        arr = []
        res = 0
        for num in nums:
            if not arr:
                arr.append(num)
            elif num > arr[-1]:
                arr.append(num)
            else:
                res = max(res, len(arr))
                arr = [num]
        res = max(res, len(arr))
        return res        