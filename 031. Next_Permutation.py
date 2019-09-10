class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # special case
        if len(nums) <= 1:
            return
        if len(nums) == 2:
            nums.sort(reverse = True)
            return
        
        # from right to left, find the index which is smaller than previous one
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] >= nums[i]:
                continue
            else:
                break
        #print(i)        

        diff = float('Inf')
        s = None
        for j in range(i, len(nums)):
            if nums[i-1] < nums[j] and nums[j]-nums[i-1] < diff:
                s = j
                diff = nums[j] - nums[i-1]
        
        if s:
            # switch i and s
            nums[i-1], nums[s] = nums[s], nums[i-1]
            # sort nums at right of s
            nums[i:] = sorted(nums[i:])
        else:
            # if s is None, means i=1 and nums[0] is largest, rearrange it into ascending order
            nums.sort()
