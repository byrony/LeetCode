# Aug 29, 2021
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        res = 0
        for n in nums:
            temp_res = 1
            # if n-1 is in the set, then sequence starting with n-1 isn't the longest
            if n-1 not in nums_set:
                while n+1 in nums_set:
                    temp_res += 1
                    n += 1
                res = max(res, temp_res)
        return res
