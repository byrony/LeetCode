class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        depth = len(nums)
        res = []
        self.dfs(nums, [], depth, res)
        return res
    
    def dfs(self, nums, arr, depth, res):
        if len(arr) < depth:
            for i, n in enumerate(nums):
                self.dfs(nums[0:i]+nums[(i+1):len(nums)], arr+[n], depth, res)
        else:
            # print(arr)
            res.append(arr)
            return
            