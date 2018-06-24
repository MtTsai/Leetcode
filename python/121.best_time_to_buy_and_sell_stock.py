class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        lowest = prices[0] if prices else 0
        for p in prices:
            max_profit = max(max_profit, p - lowest)
            lowest = min(lowest, p)
            
        return max_profit
