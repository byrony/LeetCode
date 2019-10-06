# Oct 5 2019
# partition in the way that small number paired with small number, large number with large number. Sort it first.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i%2 == 0:
                res += nums[i]
        return res
