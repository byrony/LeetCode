#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:32:59 2017

@author: caoxiang
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        num_k = len(s) // k
        for i in range(num_k):
            if i%2 == 0:
                s[k*i:k*(i+1)] = s[k*i:k*(i+1)][::-1]
        # check the less than k character left
        if num_k % 2 == 0:
            s[num_k*k : ] = s[num_k*k : ][::-1]
        elif num_k % 2 == 1:
            pass
        return ''.join(s)