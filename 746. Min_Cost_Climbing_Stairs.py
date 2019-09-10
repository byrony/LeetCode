#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:33:07 2018

@author: caoxiang
"""

# bottom up
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_step = [None]*len(cost)
        cost_step[0:2] = cost[0:2] # given length of cost is in [2,1000]
        
        self.CostNthStep(cost, cost_step, len(cost)-1)
        return min(cost_step[-1], cost_step[-2])
        

# top down    
class Solution2:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost_step = [None]*len(cost)
        cost_step[0:2] = cost[0:2] # given length of cost is in [2,1000]
        
        self.CostNthStep(cost, cost_step, len(cost)-1)
        return min(cost_step[-1], cost_step[-2])
        
    def CostNthStep(self, cost, cost_step, n):
        while n >= 0:
            if cost_step[n] != None:
                return cost_step[n]
            else:
                cost_step[n] = min(self.CostNthStep(cost, cost_step, n-1), self.CostNthStep(cost, cost_step, n-2)) + cost[n]