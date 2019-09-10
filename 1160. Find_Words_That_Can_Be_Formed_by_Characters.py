class Solution:
    def countCharacters(self, words, chars):
        dic = {}
        for c in chars:
            if c not in dic.keys():
                dic[c] = 1
            else:
                dic[c] += 1
        
        res = 0
        for word in words:
            dic_t = dic.copy()
            for w in word:
                if w in dic_t.keys() and dic_t[w] > 0:
                    dic_t[w] -= 1
                else:
                    break
            else:
                # print(word)
                res += len(word)
        return res