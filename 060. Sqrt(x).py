#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:10:54 2017

@author: caoxiang
"""

# compute the sqrt
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = (left + right)/2
        while True:
            if abs(mid*mid - x) < 0.01:
                break
            if mid*mid > x:
                right = mid
                mid = (left + right) /2
            elif mid * mid < x:
                left = mid
                mid = (mid + right)/2
        return mid
        
        
# compute the int(sqrt), e.g. input 10, output 3
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = (left+right)//2
        while True:
            print(mid)
            if mid*mid <= x < (mid+1)*(mid+1):
                break
            if mid*mid > x:
                right = mid-1
                mid = (left + right)//2
            elif mid * mid < x:
                left = mid+1
                mid = (left + right)//2
        return mid
    
def mySqrt(self, x):
    l, r = 0, x
    while l <= r:
        mid = (r+l)/2
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        elif mid*mid > x:
            r = mid - 1
        else:
            l = mid + 1

