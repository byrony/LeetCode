# Dec 22 2019

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        char_arr = []
        res = 0
        j = 0
        while j < len(s):
            cnt = len(char_arr)
            # add new char into dic, key: char, value:index
            # use char_arr to save keys in order
            while j < len(s) and s[j] not in dic.keys():
                dic[s[j]] = j
                char_arr.append(s[j])
                j += 1
                cnt += 1
            res = max(res, cnt)
            
            if j == len(s):
                return res
            
            # if meet a char exists in dict, update dic and char_arr
            for k, char in enumerate(char_arr):
                dic.pop(char_arr[k])
                if char == s[j]:
                    char_arr = char_arr[k+1:]
                    break
            
        return res
            
            