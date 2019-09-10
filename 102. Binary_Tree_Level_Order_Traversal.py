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
    
    
    

class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = []
        return self.bfs(queue, result)
        
    
    def bfs(self, queue, result):
        
        curr_queue = queue
        while curr_queue:
            curr_level_val = []
            next_queue = []
            for node in curr_queue:
                if node:
                    curr_level_val.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(curr_level_val)
            curr_queue = next_queue
            
        return result
            


# 10/8/2018
class Solution3:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(queue, res):
            while queue:
                curr_level = []
                next_level = []
                for node in queue:
                    if node is not None:
                        curr_level.append(node.val)
                        next_level.append(node.left)
                        next_level.append(node.right)
                if len(curr_level)!=0:
                    res.append(curr_level)
                queue = next_level
            return res
        res = []
        bfs([root], res)
        return res
                