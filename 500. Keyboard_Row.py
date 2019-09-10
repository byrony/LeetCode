#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:17:06 2017

@author: caoxiang
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters = {}
        row_0 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row_1 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row_2 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        all_row = [row_0, row_1, row_2]
        for i, row in enumerate(all_row):
            for letter in row:
                letters[letter] = i
        
        # check each word
        result = []
        for word in words:
            letter_line = letters[word.lower()[0]]
            for c in word.lower():
                if letters[c] != letter_line:
                    break
            else:
                result.append(word)
        return result
