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


"""
We only care the increase from local minmal to local maximal (increasing sequences).
The increased amount within all the prices is the maximal profit.

Each time checked a larger prices, compute the difference. No matter the new price
is higher or lower, update the new price to be the local minimal price.
"""
def maxProfit(prices):
    """
    compute the sum of positive difference between price[i+1] and price[i]
    """
    if not prices:
        return 0

    lowPrice = prices[0]
    profit = 0
    for i, p in enumerate(prices):
        if p > lowPrice:
            profit += p - lowPrice
            lowPrice = p
        else:
            lowPrice = p
    return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowPrice = prices[0]
        profit = 0
        for i, p in enumerate(prices):
            if p > lowPrice:
                profit += p - lowPrice
            lowPrice = p
        return profit

        
class Solution(object):
    def maxProfit(self, prices):
        """
        Compute the sum of positive difference between price[i+1] and price[i]
        """
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

result = Solution()
t=result.maxProfit(prices)
print(t)
