class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        for i in range(int(c**0.5) + 1):
            x = (c - (i**2))**0.5
            if x == int(x):
                return True
        return False
