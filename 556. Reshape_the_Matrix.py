class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums
        
        nums_flat = []
        for l in nums:
            nums_flat += l
        
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append( nums_flat[i*c +j ])
            res.append(row)
        return res
        