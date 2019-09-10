class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        curr = [root]
        res = []
        while curr != []:
            res_curr = []
            nxt = []
            for node in curr:
                if node is not None:
                    res_curr.append(node.val)        
                    nxt += node.children
            curr = nxt
            res.append(res_curr)
        return res