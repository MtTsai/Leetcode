class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        MAX_DIST = max(len(word1), len(word2))
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        def md(s1, s2):
            if not len(s1) or not len(s2):
                return max(len(s1), len(s2))

            if dp[len(s1)][len(s2)] >= 0:
                return dp[len(s1)][len(s2)]

            ret = MAX_DIST

            if s1[-1] != s2[-1]:
                # a) Insert a character
                ret = min(ret, md(s1, s2[:-1]) + 1)
                # b) Delete a character
                ret = min(ret, md(s1[:-1], s2) + 1)
                # c) Replace a character
                ret = min(ret, md(s1[:-1], s2[:-1]) + 1)
            else:
                ret = md(s1[:-1], s2[:-1])

            dp[len(s1)][len(s2)] = ret
            return ret

        return md(word1, word2)

if __name__ == "__main__":
    # a) Insert a character
    # b) Delete a character
    # c) Replace a character
    data = [(2, "abb", "bba"),
            (3, "abcd", "bssd"),
            (4, "abcdef", "afbd"),
            (0, "abcdef", "abcdef"),
            (3, "mart", "karma"),
            (0, "", "")]

    for ans, w1, w2 in data:
        out = Solution().minDistance(w1, w2)
        if ans != out:
            print "words: {} {}".format(w1, w2)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
