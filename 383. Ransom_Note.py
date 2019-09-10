#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:22:46 2017

@author: caoxiang
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        for char in magazine:
            if char not in mag:
                mag[char] = 1
            else:
                mag[char] += 1
        
        # check whether ransomNote are from magazine
        for char in ransomNote:
            if char not in mag:
                return False
            else:
                mag[char] -= 1
                if mag[char] < 0:
                    return False
        return True
        