#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 01:13:08 2017

@author: caoxiang
"""


# this method is O(n^1.5), doesn't pass the test
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0 or n ==2: # the question is: less than a non-negative number
            return 0
        
        prime_cnt = 1
        for i in range(3, n):
            num = i
            for j in range(2, int(i**0.5)+1):
                if num/j == int(num/j):
                    break
            else:
                prime_cnt += 1
        return prime_cnt
                  

class Solution2:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        
        # here is the trick: we construct list of lenght n, but actually store the number from 0 to n-1, so first and second aren't prime
        prime = [True] * n
        prime[0] = prime[1] = False # set first to False as 1 isn't prime
        for i in range(2, n):
            if prime[i] == True:
                j = i
                while i*j < n:
                    prime[i*j] = False # the trick: e.g n= 9 only need check number <=8, in the list has index 9, n[9] = 8
                    j += 1
        #print(prime)
        return sum(prime)
            
            