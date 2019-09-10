#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:42:51 2017

@author: caoxiang
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return ' '.join(arr)