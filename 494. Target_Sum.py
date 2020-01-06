# Jan 5 2020

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = [0]
        self.calculate(nums, 0, S, 0)
        return self.count[0]
        
    def calculate(self, nums, i, S, sum_):
        if i == len(nums):
            if sum_ == S:
                self.count[0] += 1
        else:
            self.calculate(nums, i+1, S, sum_ + nums[i])
            self.calculate(nums, i+1, S, sum_ - nums[i])