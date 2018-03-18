class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        coins = sorted(coins, reverse=True)
        clen = len(coins)
        MAX_COINS = (amount / coins[clen - 1]) + 1

        dp = [0] * (amount + 1)

        def find_coins(balance):
            if balance < 0:
                return MAX_COINS

            if dp[balance]:
                return dp[balance]

            if balance == 0:
                return 0

            dp[balance] = MAX_COINS
            for cid in range(clen):
                dp[balance] = min(dp[balance], find_coins(balance - coins[cid]) + 1)

            return dp[balance]

        min_coins = find_coins(amount)

        return min_coins if min_coins < MAX_COINS else -1

if __name__ == "__main__":
    data = [(3,  [1, 2, 5],           11),
            (3,  [3, 4],              10),
            (-1, [2],                 1),
            (0,  [1],                 0),
            (4,  [1, 2, 5],           20),
            (20, [1, 2, 5],           100),
            (25, [3, 8, 18],          385),
            (14, [17, 7, 31, 97],     1000),
            (87, [17, 7, 31, 97],     7899),
            (-1, [2, 6, 10],          101),
            (20, [186, 419, 83, 408], 6249),
            (25, [3, 7, 405, 436],    8839)]

    for ans, coins, amount in data:
        out = Solution().coinChange(coins, amount)
        if ans != out:
            print "coins: {}".format(coins)
            print "amount: {}".format(amount)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
