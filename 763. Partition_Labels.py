# Dec 30 2019

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # save the most right index of each letter
        dic = dict()
        for i, s in enumerate(S):
            dic[s] = i
            
        # partition happens when: index of last letter = maximum of all most right index
        res = []
        left = 0
        right = 0
        for i, s in enumerate(S):
            right = max(right, dic[s])
            if i == right:
                res.append(i+1-left)
                left = i+1
        return res