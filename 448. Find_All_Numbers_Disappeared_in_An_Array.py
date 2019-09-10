class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        # this is not O(n), should be nO(n)
        ans = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans
        """
        for n in nums:
            # note use abs() to keep the fixed position, although nums is updated each time. 
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i+1 for i, j in enumerate(nums) if j > 0]