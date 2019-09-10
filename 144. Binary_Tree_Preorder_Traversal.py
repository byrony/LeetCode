#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 01:06:50 2017

@author: caoxiang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Recursive method
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self.preorderTraversal_(root, arr)
        return arr
    def preorderTraversal_(self, root, arr):
        if root:
            arr.append(root.val)
            self.preorderTraversal_(root.left, arr)
            self.preorderTraversal_(root.right, arr)
            

# iterative method
# https://docs.python.org/2/tutorial/datastructures.html. Check Stack and Queue
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right) # note stack is last-in, first-out, so append right node first 
                stack.append(node.left)
        return result