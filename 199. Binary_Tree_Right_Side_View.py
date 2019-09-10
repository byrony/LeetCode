#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:27:16 2017

@author: caoxiang
"""

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = [(root, root.val)]
        all_levels =  self.bfs(root, queue, result)
        return [i[0] for i in all_levels]
    
    # bfs get each level nodes of the tree
    def bfs(self, root, queue, result):
        queue_thisLevel = queue
        
        while queue_thisLevel:
            queue_nextLevel = []
            level = []
            for node, val in queue_thisLevel:
                level.append(val)
                if node.right:
                    queue_nextLevel.append((node.right, node.right.val))
                if node.left:
                    queue_nextLevel.append((node.left, node.left.val))
            queue_thisLevel = queue_nextLevel
            result.append(level)
        return result
    
    
# is this problem we don't need return all the level of the tree. So just return the last node value of each level.
class Solution2:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = [(root, root.val)]
        all_levels =  self.bfs(root, queue, result)
        return all_levels
    
    # bfs get each level nodes of the tree
    def bfs(self, root, queue, result):
        queue_thisLevel = queue
        
        while queue_thisLevel:
            queue_nextLevel = []
            level = []
            for node, val in queue_thisLevel:
                level.append(val)
                if node.right:
                    queue_nextLevel.append((node.right, node.right.val))
                if node.left:
                    queue_nextLevel.append((node.left, node.left.val))
            queue_thisLevel = queue_nextLevel
            result.append(level[0]) # return the most right node value.
        return result