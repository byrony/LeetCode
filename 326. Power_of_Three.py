#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 01:54:13 2017

@author: caoxiang
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        elif 0 < n < 1:
            n = 1/n
        elif n == 0 or n == 2:
            return False
        elif n == 1:
            return True
        a, b = divmod(n, 3)
        if b != 0:
            return False
        else:
            return self.isPowerOfThree(n/3)

            
# check the type
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n <= 0:
            return False
        elif 0 < n < 1:
            n = 1/n
            
        if n*1.0/3 != float(n/3):
            return False
        else:
            return self.isPowerOfThree(n/3)