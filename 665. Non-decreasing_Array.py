# Dec 19 2019

class Solution:
    def checkPossibility(self, nums):
        modify = 0
        i = 0
        j = 1
        while i < len(nums)-1:
            if nums[j] >= nums[i]:
                i += 1
                j += 1
            else:
                modify += 1
                # check two cases: drop i or j. Plus edge case
                if i == 0:
                    nums.pop(i)
                elif i > 0 and nums[j] > nums[i-1]:
                    nums.pop(i)
                elif i > 0 and nums[j] <= nums[i-1]:
                    nums.pop(j)
            if modify > 1:
                return False
        return True