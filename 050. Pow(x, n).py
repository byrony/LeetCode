#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 03:19:53 2017

@author: caoxiang
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, (n-1)/2) * x
        