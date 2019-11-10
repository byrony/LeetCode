# stop when it finds a subtree of s equals to t
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        all_node = []
        self.dfs(s, all_node)
        for n in all_node:
            if self.isSameTree(n, t):
                return True
        return False
        
    def dfs(self, s, arr):
        if s:
            self.dfs(s.left, arr)
            self.dfs(s.right, arr)
            arr.append(s)
        else:
            arr.append(None)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# similar method, spent more time since it compares each subtree of s with t
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return s and (self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)