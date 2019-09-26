# Sep 26, 2019

class Solution:
    '''
    findPivot: different from Q1(Q33), return two pivot indexes to deal with special cases, moving low index right till a different value.
    E.g. [1,1,1,1,1,1,1,2,1,1,1], [2,2,2,2,0,2,2]
    If using the findPivot function in Q1, cannot find the unique pivot. 
    '''

    def search(self, nums: List[int], target: int) -> bool:
        pivot_0, pivot = self.findPivot(nums)
        idx_l0 = self.binarySearch(nums[0:pivot_0], target)
        idx_l = self.binarySearch(nums[pivot_0:pivot], target)
        idx_r = self.binarySearch(nums[pivot:], target)
        # print(idx_l, idx_r)
        return idx_l0 or idx_l or idx_r
    
    
    def findPivot(self, nums):
        l, r = 0, len(nums)-1
        # solve worst case: ref: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/177150/Search-in-Rotated-Sorted-Array-I-python-code
        # move l first to deal with special worst case
        while l < r-1 and nums[l] == nums[r]:
            l += 1
        l0 = l
        while l < r-1:
            mid = int((l+r)/2)
            if nums[mid] >= nums[l]:
                l = mid
            elif nums[mid] <= nums[r]:
                r = mid
            # print(l, r, nums[l], nums[r])
        #l0 is 1st pivot, r is second pivot
        return l0, r 
        
    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False