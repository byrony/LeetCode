#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 00:23:18 2017

@author: caoxiang
"""
    
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nums, rmd, combination):
            if rmd < 0:
                return
            if rmd == 0:
                result.append(combination)
                return
            for i, num in enumerate(nums):
                # i>0 accounts for the case when there is only one num
                if i>0 and nums[i] == nums[i-1]: # if num is the same as previous one, continue.
                    continue
                dfs(nums[i+1:], rmd-num, combination+[num]) # i+1 makes each num used for one time
                
        result = [] 
        candidates.sort()
        dfs(candidates, target, [])
        return result


# Sep 15, 2019
# DFS Method
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, nums, target, arr, res):
        if sum(arr) < target:
            for i, n in enumerate(nums):
                j = i-1
                if j >=0 and nums[j] == nums[i]:
                    continue
                else:
                    self.dfs(nums[i+1:], target, arr+[n], res)
        elif sum(arr) == target:
            res.append(arr)
        else:
            return