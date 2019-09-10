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