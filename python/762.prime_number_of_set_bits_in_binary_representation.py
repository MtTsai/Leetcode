class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def bits(n, base, bit_arr):
            if n != 0 and bit_arr[n] == 0:
                while base > n:
                    base >>= 1
                bit_arr[n] = bits((n - base), base, bit_arr) + 1
            return bit_arr[n]
        
        def is_prime(n):
            return True if (n == 2 or
                            n == 3 or
                            n == 5 or
                            n == 7 or
                            n == 11 or
                            n == 13 or
                            n == 17 or
                            n == 19) else False
        
        base = 1
        while (base << 1) <= R:
            base <<= 1
        
        bit_arr = [0] * (R + 1)
        bit_arr[0] = 0
        bit_arr[1] = 1
        
        ans = 0
        for i in reversed(range(L, R + 1)):
            if is_prime(bits(i, base, bit_arr)):
                ans += 1
        return ans
