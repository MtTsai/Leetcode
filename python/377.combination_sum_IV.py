class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1] * (target + 1)
        
        def dfs(remain):
            if remain < 0:
                return 0
            elif remain == 0:
                return 1
            elif dp[remain] >= 0:
                return dp[remain]
            else:
                dp[remain] = sum([dfs(remain - n) for n in nums])
                return dp[remain]
        dfs(target)
        return dp[target]
