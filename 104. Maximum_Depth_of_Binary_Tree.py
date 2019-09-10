# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        path = []
        depth = []
        depth_all_path = self.dfs(root, path, depth)
        return(max(depth_all_path))
    
    def dfs(self, root, path, depth):
        if root:
            path = path + [root.val]
        if root.right:
            self.dfs(root.right, path, depth)
        if root.left:
            self.dfs(root.left, path, depth)
        if not root.right and not root.left:
            depth.append(len(path))
            path = []
        return depth