# Nov 17 2019

# The key is: for each nood, compare the nood value to the lower bound and upper bound. 
# The bounds are updated dynamically for right sub node and left sub node. 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower = -float('Inf')
        upper = float('Inf')
        return self.dfs(root, lower, upper)
    
    def dfs(self, root, lower, upper):
        if root is None:
            return True
        # print(root.val, lower, upper, '---')
        if root.val > lower and root.val < upper:
            return self.dfs(root.left, lower, min(root.val, upper)) and self.dfs(root.right, max(root.val, lower), upper)
        else:
            return False
