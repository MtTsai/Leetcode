class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # remove zero
        nums = [1] + [n for n in nums if n] + [1]

        nlen = len(nums)

        dp = [[0] * nlen for _ in range(nlen)]

        def burst(l, r):
            if l + 1 == r:
                return 0
            elif dp[l][r]:
                return dp[l][r]

            for m in range(l + 1, r):
                dp[l][r] = max(dp[l][r], burst(l, m) + burst(m, r) + nums[l] * nums[m] * nums[r])

            return dp[l][r]

        return burst(0, nlen - 1)

if __name__ == "__main__":
    data = [(167,  [3, 1, 5, 8]),
            (36,   [6, 0, 0, 5, 0, 0]),
            (2925, [2, 4, 8, 4, 0, 7, 8, 9, 1, 2, 4, 7, 1, 7, 3])]

    for _ans, _list in data:
        result = Solution().maxCoins(_list)
        if result != _ans:
            print "Wrong Answer!!!"
            print "Output: {}".format(result)
            print "Expect: {}".format(_ans)
    print "Done"
