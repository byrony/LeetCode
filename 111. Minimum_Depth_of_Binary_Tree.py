# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Different from maximum depth of binary tree:
# note if there is only left or only right node, then return the depth of existing node + 1.
#  1
# / \
#2
# the minimal depth should be 2, not 1.

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left == None and root.right != None:
            return self.minDepth(root.right) + 1
        elif root.left != None and root.right == None:
            return self.minDepth(root.left) + 1
        else:
            depth = min(self.minDepth(root.left), self.minDepth(root.right))
            return depth + 1
