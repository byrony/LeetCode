# Jan 8 2020

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # count 0 and 1, save # of consecutive 0 and 1
        group = []
        cnt = 1
        for i in range(len(s)-1):
            j = i+1
            if s[i] == s[j]:
                cnt += 1
            else:
                group.append(cnt)
                cnt = 1
        group.append(cnt)
        
        # count each two neighbors in group, add the minimal one
        res = 0
        for i in range(len(group)-1):
            res += min(group[i], group[i+1])
        return res