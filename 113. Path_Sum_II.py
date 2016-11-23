# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        result = []
        each_tree = []
        self.pathSum_(root, sum, result, each_tree)
        return result
            
    def pathSum_(self, root, sum, result, each_tree):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        """
        why doesn't .append work? looks like if using append, 'each_tree' is modified instantly, even the `each_tree` in 
        another path is modified. However, we hope the `each_tree` of different path be independent.
        """
        if not root:
            return 
        else:
            sum -= root.val
            #each_tree.append(root.val) 
            each_tree = each_tree + [root.val]
            #print(each_tree)
            if sum ==0 and root.left == None and root.right == None:
                result.append(each_tree)
                return result
            if root.left:
                self.pathSum_(root.left, sum, result, each_tree)
            if root.right:
                self.pathSum_(root.right, sum, result, each_tree)
            
            