class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        d = 0
        out = 1.0
        if n >= 0:
            while n:
                x2d = x
                if n & 1:
                    for _ in xrange(d):
                        x2d *= x2d
                    out *= x2d
                n >>= 1
                d += 1
        else:
            n *= -1
            while n:
                x2d = x
                if n & 1:
                    for _ in xrange(d):
                        x2d *= x2d
                    out /= x2d
                n >>= 1
                d += 1

        return out
