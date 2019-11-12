# Nov 11 2019
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest_path = 0
        self.tree_depth(root, 0)
        return self.longest_path
    
    def tree_depth(self, n, depth):
        if n:
            l = self.tree_depth(n.left, depth+1)
            r = self.tree_depth(n.right, depth+1)
            # print(n.val, l, r, depth)
            path = l-depth-1 + r-depth-1
            self.longest_path = max(self.longest_path, path)
            return max(l, r)
        else:
            return depth