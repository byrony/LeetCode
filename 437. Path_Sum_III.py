# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # compute the number of path for the root node
    def pathSum_(self, root, sum, numPath):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        else:
            #print(sum, root.val)
            sum -= root.val
            if sum == 0:
                numPath += 1
            if root.left:
                numPath += self.pathSum_(root.left, sum, 0)
            if root.right:
                numPath += self.pathSum_(root.right, sum, 0)
        return numPath
        
    # traverse each node. For each node, compute the number of path under this node.
    def pathSum(self, root, sum):
        numPath = 0
        if not root:
            return 0
        else:
            ans = self.pathSum_(root, sum, numPath)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans