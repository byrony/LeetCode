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
