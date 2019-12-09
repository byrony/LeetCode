# Dec 8 2019

# similar to Q105. 
# based on postorder an inorder traversal, locate root, left subtree and right subtree

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        i = inorder.index(root_val)
        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        return root