#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 01:17:36 2018

@author: caoxiang
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.findPivot(nums)
        # print(pivot)
        # return pivot
        if pivot == None or pivot == []:
            return -1
        index1 = self.binarySearch(nums[0:pivot+1], target)
        index2 = self.binarySearch(nums[pivot+1:], target)
        if index2 !=-1:
            return index2+pivot+1
        else:
            return index1
        
        
    # find rotation point through binary search
    def findPivot(self, nums):
        left = 0 
        right = len(nums)-1
        
        while left <= right:
            #print(left, right)
            mid = (left+right)//2
            if mid+1 > len(nums)-1:
                return mid
            
            if nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] >= nums[0]: # means pivot point is on the left of mid
                left = mid+1
            elif nums[mid] < nums[0]: # means pivot point is on the right of mid
                right = mid-1
                
    
    def binarySearch(self, nums, target):
        left = 0 
        right = len(nums)-1
        while left <= right:
            #print(left, right)
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

