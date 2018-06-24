class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        t = x
        r = 0
        while t:
            r = r * 10 + t % 10
            t /= 10
        return r == x
