class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        
        curr = [(None, root)]
        depth = 0
        while curr:
            nxt = []
            for par, node in curr:
                if node is not None:
                    if node.val == x:
                        depth_x = depth
                        par_x = par
                    elif node.val == y:
                        depth_y = depth
                        par_y = par
                    nxt.append((node.val, node.left))
                    nxt.append((node.val, node.right))
            if len(nxt) > 0:
                depth += 1
            curr = nxt
        # print(depth_x, depth_y, par_x, par_y)
        return depth_x == depth_y and par_x != par_y