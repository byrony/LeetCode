#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 01:57:29 2017

@author: caoxiang
"""

def longestPalindromeSubseq(s):
    length = 0
    for i in range(len(s)):
        # odd case
        length = max(length, checkPalindrome(s, i, i))
        
        # even case
        length = max(length, checkPalindrome(s, i, i+1))
        
    return length
        
        
def checkPalindrome(s, l, r):
    leng = 0
    while l >= 0 and r <= len(s)-1:
        if s[l] == s[r]:
            leng = max(leng, r-l+1)
            l -= 1
            r += 1
        else:
            break
    return leng


s = "bbbab"
a = longestPalindromeSubseq(s)