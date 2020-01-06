# Jan 5 2020

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = dict()
        dic2 = dict()
        comm = []
        for i, l in enumerate(list1):
            dic1[l] = i
        for i, l in enumerate(list2):
            dic2[l] = i
            if l in dic1.keys():
                comm.append(l)
                
        min_idx = float('Inf')
        res = []
        for c in comm:
            if dic1[c] + dic2[c] == min_idx:
                res.append(c)
            elif dic1[c] + dic2[c] < min_idx:
                res = [c]
            min_idx = dic1[c] + dic2[c]
                
        return res
            
        