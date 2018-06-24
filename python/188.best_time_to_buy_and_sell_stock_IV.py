class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        max_trans = min(k, len(prices) / 2)
        
        if not prices or not max_trans:
            return 0
        
        if k > max_trans:
            profit = 0
            for i in range(len(prices) - 1):
                if prices[i + 1] > prices[i]:
                    profit += prices[i + 1] - prices[i]
                    
            return profit
        
        b = [-prices[0]] * max_trans
        s = [0] * max_trans
        
        for p in prices:
            for i in reversed(range(max_trans)):
                s[i] = max(s[i], b[i] + p)
                b[i] = max(b[i], s[i - 1] - p) if i > 0 else max(b[i], -p)
        
        return s[max_trans - 1]
