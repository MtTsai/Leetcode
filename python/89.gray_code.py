class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        out = [0]
        for bit in range(n):
            left_bit = 1 << bit
            out += [left_bit ^ gray_code for gray_code in reversed(out)]
        
        return out
