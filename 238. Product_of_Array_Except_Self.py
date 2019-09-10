class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1]
        right_prod = [1]
        for i in range(0, n-1):
            left_prod.append(left_prod[-1] * nums[i])
            right_prod.append(nums[n-1-i]*right_prod[-1])

        return [left_prod[i]*right_prod[n-1-i] for i in range(n)]
        