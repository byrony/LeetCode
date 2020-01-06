# Jan 4 2020

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort pair by h
        arr = sorted(people, key = lambda x: (-x[0], x[1]))
        
        # insert each pair to a new array based on k
        res = []
        for a in arr:
            res.insert(a[1], a)
        return res