# Sep 15, 2019
# DFS
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        res = []
        self.dfs(nums, k, n, [], res)
        return res
    
    def dfs(self, nums, k, target, arr, res):
        if len(arr) < k:
            for i, n in enumerate(nums):
                self.dfs(nums[i+1:], k, target-n, arr+[n], res)
        elif len(arr) == k and target == 0:
            res.append(arr)
        else:
            return