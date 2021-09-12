# Sep 11 2021
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        
        # odd
        for i in range(len(s)):
            res.append(s[i])
            il = ir = i
            while il-1 >= 0 and ir+1 <= len(s)-1:
                if s[il-1] == s[ir+1]:
                    res.append(s[il-1:ir+2])
                    il -= 1
                    ir += 1
                else:
                    break

        # even
        for i in range(len(s)-1):
            il = i
            ir = i+1
            if s[il] == s[ir]:
                res.append(s[il: ir+1])
                while il-1 >= 0 and ir+1 <= len(s)-1:
                    if s[il-1] == s[ir+1]:
                        res.append(s[il-1:ir+2])
                        il -= 1
                        ir += 1
                    else:
                        break
        # print(res)
        return len(res)



class Solution:
    def countSubstrings(self, s):
        result = []
        for i in range(len(s)):
            
            # odd case
            self.checkPalindrome(s, i, i, result)
        
            # even case
            self.checkPalindrome(s, i, i+1, result)
        
        # return result        
        return len(result)
    
    
    def checkPalindrome(self, s, l, r, result):
        while l >= 0 and r <= len(s)-1:
            if s[l] == s[r]:
                result.append(s[l:r+1])
                l -= 1
                r += 1
            else:
                break

s = 'aaa'
a = Solution()
res = a.countSubstrings(s)
print(res)