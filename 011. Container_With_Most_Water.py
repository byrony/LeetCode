#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 20:22:46 2018

@author: caoxiang
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxarea = (right - left) * min(height[left], height[right])
        
        while left <= right:
            newarea = (right - left) * min(height[left], height[right])
            maxarea = max(maxarea, newarea)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return maxarea