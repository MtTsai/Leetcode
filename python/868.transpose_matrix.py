class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        xlen = len(A)
        ylen = len(A[0])
        
        B = [[0] * xlen for _ in range(ylen)]
        
        for i in range(xlen):
            for j in range(ylen):
                B[j][i] = A[i][j]
        
        return B
