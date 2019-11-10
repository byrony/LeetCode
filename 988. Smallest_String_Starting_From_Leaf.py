# Nov 10 2019

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        
        paths = []
        self.dfs(root, '', paths)
        return min(paths)
        
    # chr(97) is 'a'; ord('a') is 97
    def dfs(self, n, path, res):
        if not n:
            return
        elif n and not n.right and not n.left:
            res.append(chr(n.val+97)+path)
        if n.left:
            self.dfs(n.left, chr(n.val+97)+path, res)
        if n.right:
            self.dfs(n.right, chr(n.val+97)+path, res)