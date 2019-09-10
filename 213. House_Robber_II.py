class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)) == 1:
            return nums[0]

        arr0 = [-1 for i in range(len(nums)-1)]
        arr1 = [-1 for i in range(len(nums)-1)]
        i = len(nums)-2
        
        return max(self.helper(nums[1:], i, arr0), self.helper(nums[:-1], i, arr1))
        
    def helper(self, nums, i, arr):
        if i < 0:
            return 0
        if arr[i] >= 0:
            return arr[i]
        else:
            temp = max(self.helper(nums, i-2, arr) + nums[i], self.helper(nums, i-1, arr))
            arr[i] = temp
            return temp