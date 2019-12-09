# Dec 2 2019

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:        
        arr = []
        self.getpath(root, '', arr)
        return sum([int(i, 2) for i in arr])
    
    def getpath(self, n, path, arr):
        if not n:
            return
        elif not n.left and not n.right:
            arr.append(path+str(n.val))
        else:
            self.getpath(n.left, path+str(n.val), arr)
            self.getpath(n.right, path+str(n.val), arr)