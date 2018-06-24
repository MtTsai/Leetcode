class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        d = 0
        t = num
        while t:
            d += 1
            t >>= 1
        return num ^ ((1 << d) - 1)
