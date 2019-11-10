class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        dic = dict()
        dic[None] = 0
        self.traverse(root, dic)
        
        del dic[None]
        freq = dict()
        for s in dic.values():
            if s not in freq:
                freq[s] = 1
            else:
                freq[s] += 1
    
        res = []
        max_freq = max(freq.values())
        for k, v in freq.items():
            if v == max_freq:
                res.append(k)
        return res
    
    # actually no need to use dic to store the subtree sum, since DP isn't necessary since left tree and right tree has no overlaps
    def traverse(self, n, dic):
        if n in dic.keys():
            return dic[n]
        elif n != None:
            dic[n] = n.val + self.traverse(n.left, dic) + self.traverse(n.right, dic)
            return dic[n]