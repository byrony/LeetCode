#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:58:36 2017

@author: caoxiang
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """        
        i = j = 0
        all_sum = 0
        while i < len(num1) or j < len(num2):
            if i < len(num1):
                n1 = ord(num1[-i-1]) - ord('0')
            else:
                n1 = 0 
            if j < len(num2):
                n2 = ord(num2[-j-1]) - ord('0')
            else:
                n2 = 0

            all_sum += (n1+n2)* 10 ** i
            i+=1
            j+=1
        return str(all_sum)
            
            
            
# don't compute sum. Much faster than previous one.
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = j = 0
        carry = 0
        result = ''
        while i < len(num1) or j < len(num2):
            if i < len(num1):
                n1 = ord(num1[-i-1]) - ord('0')
            else:
                n1 = 0 
            if j < len(num2):
                n2 = ord(num2[-j-1]) - ord('0')
            else:
                n2 = 0
            
            carry, digit_curr = divmod(n1 + n2 + carry, 10)
            result = chr(ord('0') + digit_curr) + result
            i+=1
            j+=1
        # conside the case when the highest digit has carry
        if carry == 1:
            return '1'+result
        return result