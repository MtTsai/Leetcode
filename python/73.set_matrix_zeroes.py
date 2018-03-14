class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0]) if m else 0

        zrow_set = set([])
        zcol_set = set([])

        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    zrow_set.add(row)
                    zcol_set.add(col)

        
        for row in range(m):
            for col in range(n):
                if row in zrow_set or col in zcol_set:
                    matrix[row][col] = 0

if __name__ == "__main__":
    data = [([[1,4,0],
              [2,3,0],
              [0,0,0]],
             [[1,4,2],
              [2,3,2],
              [3,2,0]])]
    for ans, mat in data:
        Solution().setZeroes(mat)
        if ans != mat:
            print "error"

    print "done"
