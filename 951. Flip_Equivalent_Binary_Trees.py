# Nov 25 2019

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (not root1 and root2):
            return False
        if root1.val != root2.val:
            return False
        if root1.val == root2.val:
            if root1.left and root2.left and root1.left.val == root2.left.val:
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            elif root1.right and root2.right and root1.right.val == root2.right.val:
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            else: 
                # flip
                return self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)