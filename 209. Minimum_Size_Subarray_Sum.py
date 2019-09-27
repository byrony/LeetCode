# Sep 27, 2019
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0 
        j = 0
        c_sum = 0
        for t in range(len(nums)):
            c_sum += nums[t]
            if c_sum >= s:
                j = t
                break
        else:
            return 0 # if c_sum is < s after loop is done
        
        res = j - i + 1
        # print(res, '*')
        
        while j < len(nums)-1 or i <= j:
            if j < len(nums) -1:
                j += 1
                c_sum += nums[j] - nums[i]
            else:
                # if j is already the last index, keep j fixed move i
                c_sum -= nums[i]
            i += 1
            
            if c_sum > s:
                while i <= j and c_sum >= s:
                    c_sum -= nums[i]
                    i += 1
                i -= 1
                c_sum += nums[i]
                # print(c_sum, res, i, j)
                res = min(res, j-i+1)
                
        return res
