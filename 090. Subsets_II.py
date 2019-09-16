# Sep 15 ,2019
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, arr, res):
        if len(nums) > 0:
            for i, n in enumerate(nums):
                j = i - 1
                if j >= 0 and nums[j] == nums[i]:
                    continue
                else:
                    res.append(arr+[n])
                    self.dfs(nums[(i+1):], arr+[n], res)
        else:
            return
        