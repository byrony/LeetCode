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


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:20:43 2017

@author: caoxiang
"""
nums = [-2,1,-3,4,-1,2,1,-5,4]

# not the dynamic programming way. Exceed time limit.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_subarray = {}
        def sum_sub_array(begin, end):
            key = str(begin) + str(end)
            if begin == end:
                sum_subarray[key] = nums[begin]
                return sum_subarray[key]
            if key in sum_subarray:
                return sum_subarray[key]
            else:
                sum_subarray[key] = nums[begin] + sum_sub_array(begin+1, end)
                return sum_subarray[key]
        
        for i in range(len(nums)-1, -1, -1):
            sum_sub_array(0, i)
        return max(sum_subarray.values())
              
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cumSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            cumSum = max(n, cumSum + n)
            maxSum = max(maxSum, cumSum)
            #print(cumSum, maxSum)
        return maxSum
        
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum = 0
        m = -float('Inf')
        for n in nums:
            sum += n
            m = max(sum, m)
            #print(m, sum)
            # if sum is negative, then drop it, restart compute the sum of the following numbers
            if sum < 0:
                sum = 0
        return m
