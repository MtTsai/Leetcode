class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        b1, s1, b2, s2 = -prices[0], 0, -prices[0], 0
        
        for p in prices:
            b1, s1, b2, s2 = max(b1, -p), max(s1, b1 + p), max(b2, s1 - p), max(s2, b2 + p)
        
        return s2
