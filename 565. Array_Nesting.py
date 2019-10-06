class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        s_saw = set()
        for i, n in enumerate(nums):
            s = set()
            s.update([n])
            j = n
            # if one number was checked before, stop
            while nums[j] not in s_saw and nums[j] not in s:
                s.update([nums[j]])
                j = nums[j]
            s_saw.update(s)    
            res = max(res, len(s))
        return res