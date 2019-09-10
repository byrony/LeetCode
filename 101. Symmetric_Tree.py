# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursively

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        else:
            return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)


# bfs with queue
class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop(0)
            if left and right and left.val == right.val:
                queue.append((left.left, right.right)) # add the pair node that need compare
                queue.append((left.right, right.left))
            elif not left and not right:
                continue
            else:
                return False
        return True