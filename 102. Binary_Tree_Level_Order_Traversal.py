#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:11:46 2016

@author: caoxiang


Note: 
create two lists to store the nodes of current level and next level; 
find the left and right nodes of the nodes in current level, and add them to next level. 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        curr_level = [root] if root else []
        ans = []
        while curr_level:
            next_level = []
            ans_curr = []
            curr_level = [node for node in curr_level]
            
            for node in curr_level:
                ans_curr.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            curr_level = next_level
            ans.append(ans_curr)
        return ans