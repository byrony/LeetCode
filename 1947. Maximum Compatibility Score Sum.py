# Aug 21 2021
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        mentor_perm = []
        self.permutations(mentors, [], mentor_perm, len(students))
        
        max_scr = 0
        for m in mentor_perm:
            scr = 0
            for i, j in zip(students, m):
                scr += self.compScore(i, j)
            max_scr = max(max_scr, scr)
        return max_scr
    
    def compScore(self, s, m):
        res = 0
        for i, j in zip(s, m):
            if i == j:
                res += 1
        return res
    
    def permutations(self, arr, curr, res, m):
        if len(curr) == m:
            res.append(curr[:])
            return
        for i in range(len(arr)):
            curr.append(arr[i])
            # print(curr, '---append---')
            self.permutations(arr[:i]+arr[i+1:], curr, res, m)
            curr.pop()
            # print(curr, '---pop---')
        