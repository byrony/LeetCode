# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: # if both are null
            return True
        elif not p or not q: # elif one of them is null
            return False
        elif p.val != q.val: # elif both are not null, compare values
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)        
        
        
        
class Solution2:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # traverse the trees
        t_p = self.dfs(p, [])
        t_q = self.dfs(q, [])
        return t_p == t_q
        #return t_p
    
    def dfs(self, tree, arr):
        if tree is not None:
            arr.append(tree.val)
            
            left = tree.left
            right = tree.right
                
            if left is None and right is None:
                pass
            elif left is not None and right is None:
                self.dfs(left, arr)
            elif left is None and right is not None:
                arr.append(None)
                self.dfs(right, arr)
            else:
                self.dfs(left, arr)
                self.dfs(right, arr)
        else:
            arr.append(None)
        return arr


# 10/10/2018
# dfs with Stack (First In Last Out)
class Solution3:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(q) == self.dfs(p)
    
    def dfs(self, root):
        if root is not None:
            res = [root.val]
        else:
            res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                if node.left and node.right:
                    res.append(node.left.val)
                    res.append(node.right.val)
                elif node.left and not node.right:
                    res.append(node.left.val)
                    res.append(None)
                elif not node.left and node.right:
                    res.append(None)
                    res.append(node.right.val)
                stack.append(node.right)
                stack.append(node.left)

        return res