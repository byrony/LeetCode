#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:24:51 2016

@author: caoxiang

Note: 
This question is the same as q102
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        curr_level = [root] if root else []
        ans = []
        while curr_level:
            next_level = []
            ans_level = []
            for node in curr_level:
                ans_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            ans.append(ans_level)
        return ans[::-1]
                    
                    
                    