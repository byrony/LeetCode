# Sep 11 2021
# Be careful about the case 'abba'. Deal with it using `i = max(i, dic[s[j]] + 1)`
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        res = []
        i, j = 0, 1
        dic = dict()
        
        while i <= len(s)-1 and j <= len(s)-1:
            if s[i] not in dic.keys():
                dic[s[i]] = i
            while j <= len(s)-1:
                # print(i, j)
                if s[j] not in dic.keys():
                    dic[s[j]] = j
                    j += 1
                else:
                    res.append((i, j-1))
                    i = max(i, dic[s[j]] + 1)
                    dic[s[j]] = j
                    j += 1
                    break
            if j == len(s):
                res.append((i, j-1))
                
        # print(res)
        long_sub_idx = sorted(res, key=lambda x: x[1]-x[0], reverse=True)
        return long_sub_idx[0][1] - long_sub_idx[0][0] + 1



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
            
            