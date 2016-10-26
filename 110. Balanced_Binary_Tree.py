# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# if we use the maxDepth() of question 104, then it's slow
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
            return depth + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False

