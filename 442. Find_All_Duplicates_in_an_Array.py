class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # unique = set()
        # res = []
        # for n in nums:
        #     if n not in unique:
        #         unique.update([n])
        #     else:
        #         res.append(n)
        # return res
        
        # method 2: constant space
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -1 * nums[abs(nums[i])-1]
            else:
                res.append(abs(nums[i]))
        return res