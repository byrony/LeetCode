# backtracking. Time Exceeded Limit
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = nums[0]
        if n >= len(nums)-1:
            return True
        
        for i in range(n, 0, -1):
            if self.canJump(nums[i:]):
                return True
        return False


# dymanic programming, cannot pass last case
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dic = dict()
        res = self.helper(nums, 0, dic)
        return res      
        
    def helper(self, nums, idx, dic):
        n = nums[idx]
        if n >= len(nums)-1-idx:
            dic[idx] = True
            return True

        if idx in dic.keys():
            return dic[idx]
        else:
            for i in range(idx+n, idx, -1):
                res = self.helper(nums, i, dic)
                dic[idx] = res
                if res:
                    return True
        return False