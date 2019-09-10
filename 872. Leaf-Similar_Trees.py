class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leafGenerator(root1) == self.leafGenerator(root2)
        
    def leafGenerator(self, root):
        nodes = [root]
        leaf = []
        while nodes != []:
            node = nodes.pop()
            if not node.left and not node.right:
                leaf.append(node.val)
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return leaf