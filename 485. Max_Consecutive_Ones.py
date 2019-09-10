#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:43:22 2017

@author: caoxiang
"""

# here I just generate the rank of all consecutive number. It can be simplified to only return the max number.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
            
        rank = [nums[0]] # if 1st number is 1, then consecutive number is 1. Otherwise set it to be 0
        cons = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 1 and nums[i] == nums[i-1]:
                cons += 1
            elif nums[i] == 1 and nums[i] != nums[i-1]:
                cons = 1
            else:
                cons = 0
            rank.append(cons)
        #print(rank)
        return max(rank)
