class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_pos = 1
        if divisor < 0:
            divisor = 0 - divisor
            is_pos ^= 1
        if dividend < 0:
            dividend = 0 - dividend
            is_pos ^= 1
        
        if divisor > dividend:
            return 0
        if divisor == 0:
            return MAX_INT
        
        ans = 0
        base = 1
        while (divisor << 1) < dividend:
            divisor <<= 1
            base <<= 1
            
        while base:
            while divisor <= dividend:
                dividend -= divisor
                ans += base
            divisor >>= 1
            base >>= 1
        
        if ans > 2147483647:
            return 2147483647 if is_pos else -2147483648
        else:
            return ans if is_pos else (0 - ans)
