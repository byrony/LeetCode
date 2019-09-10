class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.permute(nums)
        
    
    def permute(self, nums):
        res = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            j = i - 1
            # if the number is the same as previous one (already used), then move to next number
            if j >= 0 and nums[j]==nums[i]:
                continue
            nums_new = nums[0:i] + nums[i+1:]
            for n in self.permute(nums_new):
                res.append([nums[i]] + n)
        return res
        
        
        