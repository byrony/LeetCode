class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # cnt0, cnt1, cnt2 = 0, 0, 0
        # for n in nums:
        #     if n == 0:
        #         cnt0 += 1
        #     elif n == 1:
        #         cnt1 += 1
        #     else:
        #         cnt2 += 1
        # print(cnt0, cnt1, cnt2)
        # for i in range(len(nums)):
        #     if i < cnt0:
        #         nums[i] = 0
        #     elif i < cnt0+cnt1:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        # return nums
        
        l = 0
        h = len(nums) - 1
        i = 0
        while i <= h:
            # if nums[i] is 0, swap it with low index
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            # if nums[i] is 2, swap it with high index
            elif nums[i] == 2:
                nums[h], nums[i] = nums[i], nums[h]
                h -= 1
            else:
                i += 1
        print(l, i, h)
        return nums
            