# Jan 5 2020

# O(n^2)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            var = -1
            
            for j in range(i+1, len(nums)):
                if nums[j] > n:
                    var = nums[j]
                    break
            else: # no greater element is found in [i+1, len(nums)]
                for j in range(i):
                    if nums[j] > n:
                        var = nums[j]
                        break
            
            res.append(var)
        return res


# O(n) using Stack
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        res = [-1]*len(nums)
        
        # find next greater element for each num in nums from right to left
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if len(stack) == 0:
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])
        
        return res