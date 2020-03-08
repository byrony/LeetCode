# Feb 2 2020

# Exceeded Time Limit. O(n^2)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_i = float('Inf')
        for j in range(len(nums)):
            min_i = min(min_i, nums[j])
            for k in range(j+1, len(nums)):
                if min_i < nums[k] and nums[k] < nums[j]:
                    return True
        return False


# Ref: https://leetcode.com/problems/132-pattern/discuss/94081/10-line-Python-Solution
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_ = -float('Inf')
        stack = []
        for n in nums[::-1]:
            if n < min_:
                return True
            while stack and stack[-1] < n:
                min_ = stack.pop()
            stack.append(n)
            # print(stack)
        return False