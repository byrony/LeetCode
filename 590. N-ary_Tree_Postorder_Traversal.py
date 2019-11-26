# Nov 25 2019

class Solution:
    def postorder(self, root: 'Node') -> List[int]:        
        ## similiar to preorder, but go right
        if not root:
            return []
    
        arr = []
        stack = [root]
        while stack:
            node = stack.pop()
            arr.append(node.val)
            for n in node.children:
                stack.append(n)
        return arr[::-1]
                