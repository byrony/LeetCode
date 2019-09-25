class Solution:
    def numEquivDominoPairs(self, dominoes):
        dic = dict()
        for d in dominoes:
            tmp_k = frozenset(d)
            if tmp_k not in dic.keys():
                dic[tmp_k] = 1
            else:
                dic[tmp_k] += 1
        
        res = 0
        for k, v in dic.items():
            res += v*(v-1)/2
        return int(res)