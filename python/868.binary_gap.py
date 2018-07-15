class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        
        d = 0
        last = -1
        while N:
            if N & 1:
                if last >= 0:
                    ans = max(ans, d - last)
                last = d
            d += 1
            N >>= 1
        return ans
