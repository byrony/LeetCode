# refer the code by caikehe 
# https://discuss.leetcode.com/topic/20844/python-easy-to-understand-solution-with-comments-from-middle-to-two-ends

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):

            # odd case
            tmp = self.checkPalindrome(s, i, i)
            if len(tmp) > len(result):
                result = tmp

            # even case
            tmp = self.checkPalindrome(s, i, i+1)
            if len(tmp) > len(result):
                result = tmp

        return result


    def checkPalindrome(self, s, l, r):
        while l >= 0 and r <= len(s)-1:
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r] # here is a trick: if break, return the previous l which is new l plus 1


s = 'bab'
a = Solution()
res = a.longestPalindrome(s)
print(res)


# Jan 11 2020

# Dynamic Programming: Bottom-up
# use a set() to save all Palindromic Substring. Time Limit Exceeded...
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # check edge case when length(s) is 1 or 2 or 3
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        
        # check each substring of length >=3
        # initial all one and two letters palindrome substring
        allPal = set('')
        allPal.update([chr(i) for i in range(127)])
        allPal.update([chr(i)*2 for i in range(127)])
        
        l, r = 0, 0
        for k in range(2, len(s)):
            for i in range(len(s)-k):
                j = i + k
                if s[i] == s[j] and s[i+1 : j] in allPal:
                    allPal.add(s[i: j+1])
                    if j+1-i > r - l:
                        l, r = i, j+1
                elif s[i+1:j+1] in allPal:
                    if j-i > r - l:
                        l, r = i+1, j+1
                elif s[i:j] in allPal:
                    if j-i > r - l:
                        l, r = i, j
                elif s[i+1 : j] in allPal:
                    if j-i-1 > r - l:
                        l, r = i+1, j
        return s[l:r]
                
# DP: Bottom-up
# use a 2-D matrix to save the whether substring s[i:j] is palindrome
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # check edge case when length(s) is 1
        if len(s) == 1:
            return s
        
        # check each substring of length >=2
        n = len(s)
        allPal = [[0]*n for _ in range(n)]
        for i in range(n):
            allPal[i][i] = True
        
        l, r = 0, 0
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                # edge case when length of palindrome is 2
                if k==1 and s[i]==s[j]:
                    allPal[i][j] = True
                    l, r = i, j
                elif s[i] == s[j] and allPal[i+1][j-1] == True:
                    allPal[i][j] = True
                    if j-i > r - l:
                        l, r = i, j
        return s[l:r+1]
                

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # check edge case when length(s) is 1
        if len(s) == 1:
            return s
        
        # check each substring of length >=2
        n = len(s)
        allPal = [[0]*n for _ in range(n)]
        for i in range(n):
            allPal[i][i] = True
        
        l, r = 0, 0
        for i in range(n):
            for j in range(0, i):
                if j==i-1 and s[i]==s[j]:
                    allPal[j][i] = True
                    if i-j > r - l:
                        l, r = j, i
                if s[i]==s[j] and allPal[j+1][i-1]:
                    allPal[j][i] = True
                    if i-j > r - l:
                        l, r = j, i
        return s[l:r+1]