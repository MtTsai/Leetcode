class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        n = x ^ y
        
        hamming_distance = 0
        while n > 0:
            if n & 1:
                hamming_distance += 1
            n >>= 1
            
        return hamming_distance
