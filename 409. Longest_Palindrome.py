class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = dict()
        for letter in s:
            if letter in dic.keys():
                dic[letter] += 1
            else:
                dic[letter] = 1
        
        res = 0
        has_odd = False
        for k, v in dic.items():
            if v%2 == 0:
                res += v
            else:
                res += v-1
                has_odd = True
        return res+1 if has_odd else res