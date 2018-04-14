class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        hold, idle, cooldown = -prices[0] if prices else 0, 0, 0
        for p in prices:
            hold, idle, cooldown = max(hold, idle - p), max(idle, cooldown), hold + p
        return max(idle, cooldown)
        
    def _maxProfit(self, prices):
        plen = len(prices)
        dp = [-1] * plen
        
        def mp(n):
            if n >= plen:
                return 0

            if dp[n] >= 0:
                return dp[n]

            dp[n] = 0
            low = prices[n]
            for i in range(n + 1, plen):
                if prices[i] <= low:
                    low = prices[i]
                    continue

                dp[n] = max(dp[n], mp(i + 2) + prices[i] - low)
            
            return dp[n]

        return mp(0)

if __name__ == "__main__":
    data = [(0, [2, 1]),
            (3, [1, 4, 2]),
            (3, [1, 2, 3, 0, 2]),
            (4, [0, 1, 3, 2, 4]),
            (5, [0, 3, 1, 2, 4]),
            (5, [0, 3, 1, 4, 5])]

    for ans, prices in data:
        out = Solution().maxProfit(prices)
        if out != ans:
            print "expect: {}".format(ans)
            print "output: {}".format(out)
    print "Done"
