#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 01:59:26 2017

@author: caoxiang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.postorderTraversal_(root, arr)
        return arr
    
    def postorderTraversal_(self, root, arr):
        if root:
            self.postorderTraversal_(root.left, arr)
            self.postorderTraversal_(root.right, arr)
            arr.append(root.val)