#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 20:57:14 2017

@author: caoxiang
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #lowerLetter = [chr(i) for i in range(97, 123)]
        #upperLetter = [chr(i) for i in range(65, 91)]
        if len(word) == 1:
            return True
        
        first = ord(word[0])
        if first >= 97:
            for i, c in enumerate(word[1:]):
                if ord(c) <= 91:
                    return False
            return True
        elif first <= 91: # 1st uppercase, the rest must be the same case
            tmp = []
            for i in list(word[1:]):
                if ord(i) >= 97:
                    tmp.append(False)
                else:
                    tmp.append(True)
            if len(set(tmp)) == 1:
                return True
            else:
                return False
            
            
            