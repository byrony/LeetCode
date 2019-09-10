class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = [root]
        
        res = []
        level = 1
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            stack.extend(node.children)
            lev
        return res