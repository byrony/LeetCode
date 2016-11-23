# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Note:
This quesiton is slightly different from q 102, only need adjust the sequence of added node value in each level 
based on the level number.
"""

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        curr_level = [root] if root else []
        ans = []
        level = 0
        while curr_level:
            ans_curr = []
            next_level = []
            for node in curr_level:
                # add the node value of current level based on number of level
                if level % 2 == 0:
                    ans_curr.append(node.val)
                else:
                    ans_curr = [node.val] + ans_curr
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            curr_level = next_level
            level += 1
            ans.append(ans_curr)
        return ans