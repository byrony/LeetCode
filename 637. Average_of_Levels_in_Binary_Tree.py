# Nov 17 2019

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return
        
        res = []
        self.bfs([root], res)
        # print(res)    
        return [1.0*sum(i)/len(i) for i in res]
    
    def bfs(self, curr, res):
        nxt = []
        curr_val = []
        while curr:
            n = curr.pop()
            curr_val.append(n.val)
            if n.left:
                nxt.append(n.left)
            if n.right:
                nxt.append(n.right)
            if len(curr) == 0:
                res.append(curr_val)
                curr = nxt
                curr_val = []
                nxt = []