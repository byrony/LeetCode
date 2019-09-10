#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:40:32 2016

@author: caoxiang
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []
        each_path = None
        return self._binaryTreePath(root, ans, each_path)
    
    def _binaryTreePath(self, root, ans, each_path):
        if not root:
            return None
        else:
            #each_path.append(root.val)
            each_path = str(each_path)  + '->' + str(root.val)
            if root.left == None and root.right == None:
                ans.append(each_path[6:]) # [6:] omit the substring 'None->' at the head
            self._binaryTreePath(root.left, ans, each_path)
            self._binaryTreePath(root.right, ans, each_path)
            
        return ans
        

"""
See here for different solutions:
    http://blog.csdn.net/coder_orz/article/details/51706119
"""
        
class Solution2:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []
        each_path = []
        self._binaryTreePath(root, ans, each_path)
        return ans
    
    def _binaryTreePath(self, root, ans, each_path):
        if not root:
            return
        else:
            each_path.append(str(root.val))
            if root.left == None and root.right == None:
                ans.append('->'.join(each_path))
                print(ans)
            self._binaryTreePath(root.left, ans, each_path)
            self._binaryTreePath(root.right, ans, each_path)
            
            each_path.pop()