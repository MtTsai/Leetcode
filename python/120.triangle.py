class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for row_idx in reversed(range(len(triangle) - 1)):
            row = triangle[row_idx]
            row_next = triangle[row_idx + 1]
            for col_idx in range(len(row)):
                row[col_idx] += min(row_next[col_idx], row_next[col_idx + 1])
                
        return triangle[0][0]
