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


# Mar 7, 2020
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, res, [], target)
        return res
    
    def dfs(self, candidates, res, path, target):
        if target == 0:
            res.append(path)
            return
        elif target < 0:
            return
        else:
            for i, c in enumerate(candidates):
                self.dfs(candidates[i:], res, path+[c], target-c)


# Aug 14, 2021
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, candidates, target, path, res):
        if target == 0:
            # Note need append the elements of path rather than the reference, e.g. path[:], path.copy()
            # since path was keeping modified
            res.append(path[:])
            return
        else:
            for i, c in enumerate(candidates):
                if c > target:
                    return
                # only check [i:] to avoid duplicate results
                path.append(c)
                # print(path, '----append----')
                self.dfs(candidates[i:], target-c, path, res)
                path.pop()
                # print(path, '----pop----')
