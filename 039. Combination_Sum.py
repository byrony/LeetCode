#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:41:31 2017

@author: caoxiang
"""

def dfs2(candidates, rmd, combination):
        if rmd < 0:
            return None
        for number in candidates:
            if number == rmd:
                result.append(combination)
                return None
            elif number < rmd:
                dfs(candidates, rmd-number, combination+[number])

class Solution(object):
    def combinationSum(self, candidates, target):
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
                dfs(nums[i:], rmd-num, combination+[num]) # just pass nums[i:] to avoid duplicate combinations
                
        result = [] 
        dfs(candidates, target, [])
        return result