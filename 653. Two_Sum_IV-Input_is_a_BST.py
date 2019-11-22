# Nov 21 2019

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        queue = [root]
        s = set()
        while queue:
            n = queue.pop(0)
            if k-n.val in s:
                return True
            else:
                s.add(n.val)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
            
        return False