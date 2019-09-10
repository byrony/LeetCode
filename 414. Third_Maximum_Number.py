#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:15:43 2016

@author: caoxiang
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = -float('Inf')
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif a > n > b:
                b, c = n, b
            elif b > n > c:
                c = n
        # print(a,b,c)
        return c if c != -float('inf') else a
                
def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # by comparing the nums, we avoiding including the equal numbers.
    a = b = c = -float('Inf')
    for n in nums:
        if n > a:
            a, b, c = n, a, b
        elif a > n > b:
            b, c = n, b
        elif b > n > c:
            c = n
    #print(a,b,c)
    return c if c == -float('inf') else a
nums = [3,2,2,1, 5,5,8]