# Dec 8 2019

# based on preorder an inorder traversal, locate root, left subtree and right subtree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        for i, val in enumerate(inorder):
            if val == root_val:
                root.left = self.buildTree(preorder[0:i], inorder[0:i])
                root.right = self.buildTree(preorder[i:], inorder[i+1:])
                break
        return root


# faster if using .index() to find index of root
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        i = inorder.index(root_val)
        root.left = self.buildTree(preorder[0:i], inorder[0:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])
        return root