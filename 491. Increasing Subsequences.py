# Aug 21 2020
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, i, curr, res):
        if len(curr) >= 2:
            res.add(tuple(curr[:]))
        if i >= len(nums):
            return
            
        for j in range(i, len(nums)):
            if len(curr) == 0 or nums[j] >= curr[-1]:
                curr.append(nums[j])
                # print(curr, '---append---')
                self.dfs(nums, j+1, curr, res)
                curr.pop()
                # print(curr, '---pop---')
