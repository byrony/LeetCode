#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:35:43 2017

@author: caoxiang
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] +=1
        
        for c in t:
            if c not in dic or dic[c]==0:
                return c
            else:
                dic[c] -=1 # if character exists, delete its value by one