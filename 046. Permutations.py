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
            

# Mar 7, 2020
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.k = len(nums)
        res = []
        self.dfs(res, [], nums)
        return res
    
    def dfs(self, res, path, nums):
        if len(path) == self.k:
            res.append(path)
            return
        else:
            for i, n in enumerate(nums):
                self.dfs(res, path+[n], nums[:i]+nums[i+1:])
