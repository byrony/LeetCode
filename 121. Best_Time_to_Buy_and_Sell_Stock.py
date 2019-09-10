#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     29/06/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


prices = [7,1,5,3,6,4]

# exceed time limit
def maxProfit(prices):
    mProfit = -float('Inf')
    highestPrice_index = 1

    temp = highestPrice_index
    for i in range(len(prices)-1):
        begin_index = max(temp, i+1)
        for j in range(begin_index, len(prices)):
            if prices[j] - prices[i] > mProfit:
                mProfit = prices[j] - prices[i]
                highestPrice_index = j
        temp = highestPrice_index
        #print(temp)

    if mProfit > 0:
        return mProfit
    else:
        return 0

class Solution(object):
    def maxProfit(self, prices):
        """
        Brute force. Exceed time limit (the last test case)
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit

# http://chaoren.is-programmer.com/posts/43595.html
def maxProfit2(prices):
    """
    Solution: for each point, we want to find the maximal difference between it and the previous points.
    """
    if not prices:
        return 0

    lowPrice = prices[0]
    maxProfit = 0
    for i in range(len(prices)):
        lowPrice = min(lowPrice, prices[i])
        maxProfit = max(prices[i]-lowPrice,  maxProfit)
    return maxProfit



# 6/29/2019
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        profit = [0 for i in range(len(prices))]
        
        # from left to right, save maximum profit of list prices[0:i] in profit[i]
        min_price = prices[0]
        for i in range(1, len(prices)):
            profit[i] = max(profit[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
            #print(profit)
        return profit[-1]
            