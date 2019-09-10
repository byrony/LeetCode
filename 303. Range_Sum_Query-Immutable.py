class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.dic = dict()
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if j > i:
#                     self.dic[(i,j)] = self.dic[(i,j-1)] + self.nums[j]
#                 else:
#                     self.dic[(i,j)] = self.nums[i]
 
#     def sumRange(self, i: int, j: int) -> int:
#         return self.dic[(i,j)]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


    def __init__(self, nums: List[int]):
        if nums:
            self.dic = [0] + [0 for i in range(len(nums))]
        else:
            self.dic = []
        for i in range(len(nums)):
            self.dic[i+1] = self.dic[i] + nums[i]
 
    def sumRange(self, i: int, j: int) -> int:
        return self.dic[j+1] - self.dic[i]