# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: # if both are null
            return True
        elif not p or not q: # elif one of them is null
            return False
        elif p.val != q.val: # elif both are not null, compare values
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)        