# Dec 14 2019

# Ugly solution. Didn't handle the edge cases elegantly

class Solution:
    def numDecodings(self, s: str) -> int:
        # special test cases
        if s[0] == '0':
            return 0
        if len(s)>1 and s[-1]=='0' and s[-2]=='0':
            return 0
        if len(s)>1 and s[-2] > '2' and s[-1] == '0':
            return 0
        
        # dic saves the decode ways of substring s[i:], key is i
        dic = dict()
        dic[len(s)-1] = 1 if s[-1]!='0' else 0
        if (s[len(s)-2] =='1' or s[len(s)-2]=='2') and s[len(s)-1] == '0':
            dic[len(s)-2] = 1
        elif s[len(s)-2 :] > '26':
            dic[len(s)-2] = 1
        elif s[len(s)-2 :] <= '26' and s[len(s)-2 :]>='11':
            dic[len(s)-2] = 2
        else:
            dic[len(s)-2] = 1

        invalid = [False]
        self.dp(s, 0, dic, invalid)
        # print(dic, invalid)
        return dic[0] if not invalid[0] else 0
        
    def dp(self, s, i, dic, invalid):
        # compute the decode ways of s[i:]
        if i in dic.keys():
            return dic[i]
        
        elif s[i]=='0' and s[i+1]>'0':
            tmp = self.dp(s, i+1, dic, invalid)
        elif (s[i]=='1' or s[i]=='2') and s[i+1]=='0':
            tmp = self.dp(s, i+1, dic, invalid)
        elif s[i+1]=='0':
            invalid[0] = True
            tmp = 0
        elif s[i:i+2] <= '26':
            tmp = self.dp(s, i+1, dic, invalid) + self.dp(s, i+2, dic, invalid)       
        else:
            tmp = self.dp(s, i+1, dic, invalid)
        dic[i] = tmp
        return tmp