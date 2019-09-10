class Solution:
    def rob(self, nums: List[int]) -> int:
        # create a dict to store rob money for sub nums, len(nums) is key
        dic = dict()
        return self.helper(nums, dic)
    
    def helper(self, nums, dic):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            if len(nums) in dic.keys():
                return dic[len(nums)]
            else:
                temp = max(self.helper(nums[2:], dic)+ nums[0], self.helper(nums[1:], dic))
                dic[len(nums)] = temp
                return temp
        
        