#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 02:42:44 2017

@author: caoxiang
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num == 2 or num == 3:
            return False
        elif num == 1:
            return True
        a, b = divmod(num, 4)
        if b != 0:
            return False
        else:
            return self.isPowerOfFour(num/4)
        

# use bit manipulation. 
# For binary numberof the power of four, the number of zero is even
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        else:
            if num & (num - 1) == 0 and len(bin(num)[3:]) % 2 == 0:
                return True
            else:
                return False
        