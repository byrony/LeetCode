#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:50:40 2017

@author: caoxiang
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        return self.searchInsert_(nums, target, 0, len(nums))
        
    def searchInsert_(self, nums, target, left, right):
        mid = int((left+right)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid-1] < target < nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.searchInsert_(nums, target, left, mid)
        elif target > nums[mid]:
            return self.searchInsert_(nums, target, mid, right)       


## 10/10/2018
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        return left
        