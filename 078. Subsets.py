#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:43:28 2017

@author: caoxiang
"""

# method 1: bfs
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist + [nums[i]])
        res = []
        dfs(0, 0, [])
        return res
        
        
S = [1,2,3]
def dfs(depth, start, valuelist):
    res.append(valuelist)
    print(depth, start, valuelist)
    print(res)
    if depth == len(S):
        return
    for i in range(start, len(S)):
        dfs(depth+1, i+1, valuelist+[S[i]])

res = []
dfs(0, 0, [])


"""
Draw plot to understand it clearly. It's correct.
1.  dfs(0,0)
      |
2.  dfs(1,1) ->                     6. dfs(1,2) ->  8. dfs(1,3) Stop
      |                                   |
3.  dfs(2,2) -> 5. dfs(2,3) Stop    7. dfs(2,3) Stop
      |
4.  dfs(3,3)  Stop

0 0 []
[[]]
1 1 [1]
[[], [1]]
2 2 [1, 2]
[[], [1], [1, 2]]
3 3 [1, 2, 3]
[[], [1], [1, 2], [1, 2, 3]]
2 3 [1, 3]
[[], [1], [1, 2], [1, 2, 3], [1, 3]]
1 2 [2]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
2 3 [2, 3]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
1 3 [3]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
"""

