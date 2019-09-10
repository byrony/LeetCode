class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # save A, B number pairs into dictionary
        dic_ab = dict()
        for a in A:
            for b in B:
                if a+b in dic_ab:
                    dic_ab[a+b] += 1
                else:
                    dic_ab[a+b] = 1
        
        res = 0
        for c in C:
            for d in D:
                temp = 0-(c+d)
                if temp in dic_ab.keys():
                    res += dic_ab[temp]
        return res