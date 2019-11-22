# Nov 21 2019

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.bfs([root], res)
        return max(res)
        
    def bfs(self, stack, res):
        # bfs finds the width of each level
        while stack:
            nxt = []
            value = []
            for n in stack:
                if n:
                    value.append(n.val)
                else:
                    value.append(None)
                if n and n.left:
                    nxt.append(n.left)
                else:
                    nxt.append(None)
                if n and n.right:
                    nxt.append(n.right)
                else:
                    nxt.append(None)
                    
            # remove the None in head and tail
            while nxt and nxt[0] is None:
                nxt.pop(0)
            while nxt and nxt[-1] is None:
                nxt.pop()
            stack = nxt
            
            res.append(len(value))
        