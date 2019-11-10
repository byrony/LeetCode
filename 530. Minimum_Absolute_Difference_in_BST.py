# Nov 10 2019

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        self.inorder_traverse(root, arr)
        res = float('Inf')
        for i in range(len(arr)-1):
            j = i + 1
            res = min(res, arr[j]-arr[i])
        return res
        
    def inorder_traverse(self, root, arr):
        if not root:
            return
        else:
            self.inorder_traverse(root.left, arr)
            arr.append(root.val)
            self.inorder_traverse(root.right, arr)