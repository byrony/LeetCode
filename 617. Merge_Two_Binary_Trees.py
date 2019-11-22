# Nov 17 2019

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = t1
        if not t1:
            return t2
        if not t2:
            return t1
        if t1 and t2:
            t3.val = t1.val + t2.val
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        return t3