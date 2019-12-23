# Dec 20 2019

# reference: https://www.youtube.com/watch?v=7DKFpWnaxLI

# iteration
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # lis[i] saves the LIS of subsequence of nums[0:i]
        # The subsequence MUST ending with nums[i]
        # Based on the definition, length of subsequence ending with nums[i] at least is 1, fill lis with 1
        lis = [1 for i in range(len(nums))] 
        # lis[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        # print(lis)
        return max(lis)