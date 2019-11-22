# Nov 12 2019
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        arr = []
        self.inorder_traverse(root, arr)
        dic = dict()
        for a in arr:
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
        max_f = max(dic.values())
        return [k for k, v in dic.items() if v == max_f]
        
    
    def inorder_traverse(self, root, arr):
        if root:
            self.inorder_traverse(root.left, arr)
            arr.append(root.val)
            self.inorder_traverse(root.right, arr)
        else:
            return