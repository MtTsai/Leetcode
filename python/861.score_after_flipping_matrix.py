class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row_len = len(A)
        col_len = len(A[0])
        for row_idx in range(row_len):
            if A[row_idx][0] == 0:
                for col_idx in range(col_len):
                    A[row_idx][col_idx] ^= 1

        for col_idx in range(1, col_len):
            count = 0
            for row_idx in range(row_len):
                count += A[row_idx][col_idx]
            if count > row_len / 2:
                continue
            else:
                for row_idx in range(row_len):
                    A[row_idx][col_idx] ^= 1

        ans = 0
        for row in A:
            ans += int(''.join([str(i) for i in row]), 2)
            
        return ans
