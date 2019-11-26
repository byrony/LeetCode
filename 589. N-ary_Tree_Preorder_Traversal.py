# Nov 23 2019

# Recursive
class Solution:
    def preorder(self, root: 'Node') -> List[int]:        
        arr = []
        self.traverse(root, arr)
        return arr
    
    def traverse(self, n, arr):
        if n:
            arr.append(n.val)
            for node in n.children:
                self.traverse(node, arr)
        else:
            return


# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            arr.append(node.val)
            for n in node.children[::-1]:
                stack.append(n)
        return arr