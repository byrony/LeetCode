# Nov 17 2019

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        self.tree_path(root, [], paths, p, q)
        # print([[p.val for p in n] for n in paths])
        # two paths which contain p and q separately returned
        
        path_p, path_q = paths[0], paths[1]
        i = 0
        while i < min(len(path_p), len(path_q)):
            if path_p[i] == path_q[i]:
                i += 1
            else:
                break
        return path_p[i-1]

    def tree_path(self, n, path, paths, p, q):
        if n is None:
            return
        if n.val == p.val or n.val == q.val:
            paths.append(path+[n])
        self.tree_path(n.left, path + [n], paths, p, q)
        self.tree_path(n.right, path + [n], paths, p, q)  