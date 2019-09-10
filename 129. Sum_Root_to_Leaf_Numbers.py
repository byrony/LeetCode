#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 02:04:51 2017

@author: caoxiang
"""

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        all_path = []
        path = []
        self.dfs(root, path, all_path)
        
        result = 0
        for p in all_path:
            result += self.compute_sum(p)
        return result
        
    def dfs(self, root, path, all_path):
        if not root:
            return
        path = path + [root.val]
        if root.left:
            self.dfs(root.left, path, all_path)
        if root.right:
            self.dfs(root.right, path, all_path)
        if not root.left and not root.right:
            all_path.append(path)
            return all_path
        
    def compute_sum(self, arr):
        length = len(arr)
        rst = 0
        for i, a in enumerate(arr):
            rst += a* 10**(length-1-i)
        return rst