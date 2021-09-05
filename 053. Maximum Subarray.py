# Sep 2, 2021
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cumsum = -float('Inf')
        maxsum = -float('Inf')
        
        for n in nums:
            if cumsum < 0:
                cumsum = n
            else:
                cumsum += n
            maxsum = max(maxsum, cumsum)
            # print(n, maxsum, cumsum)
        return maxsum