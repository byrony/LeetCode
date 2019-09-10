class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        self.traversal(root, res)
        dic = {}
        for i, item in enumerate(res):
            key = res[i]
            if i > 0:
                res[i] += res[i-1]
            dic[key] = res[i]
        
        # modify tree
        self.modify_tree(root, dic)
        return root
    
    def modify_tree(self, root, dic):
        if root:
            root.val = dic[root.val]
            self.modify_tree(root.left, dic)
            self.modify_tree(root.right, dic)
        
    def traversal(self, root, res):
        if root:
            self.traversal(root.right, res)
            res.append(root.val)
            self.traversal(root.left, res)


# method 2: reverse inorder traversal, cummulatively compute the number need added to each node
class Solution2:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder_rev(root, 0)
        return root

    def inorder_rev(self, root, add):
        if root:
            add = self.inorder_rev(root.right, add)
            add += root.val
            root.val = add
            #print(root.val, add)
            add = self.inorder_rev(root.left, add)
        return add