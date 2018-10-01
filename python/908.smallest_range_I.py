class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        Bmax = A[0] - K
        Bmin = A[0] + K
        
        for v in A:
            Bmax = max(Bmax, v - K)
            Bmin = min(Bmin, v + K)
            
        return Bmax - Bmin if Bmax > Bmin else 0
