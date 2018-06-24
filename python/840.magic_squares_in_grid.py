class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ylen = len(grid)
        xlen = len(grid[0]) if ylen else 0
        if ylen < 3 or xlen < 3:
            return 0

        def is_magic_square(x, y):
            for i in range(3):
                for j in range(3):
                    if grid[y + i][x + j] > 9 or grid[y + i][x + j] < 1:
                        return False
            t =     (grid[y]    [x]     + grid[y + 1][x]     + grid[y + 2][x]    )
            if t != (grid[y]    [x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1]):
                return False
            if t != (grid[y]    [x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2]):
                return False
            if t != (grid[y]    [x]     + grid[y]    [x + 1] + grid[y]    [x + 2]):
                return False
            if t != (grid[y + 1][x]     + grid[y + 1][x + 1] + grid[y + 1][x + 2]):
                return False
            if t != (grid[y + 2][x]     + grid[y + 2][x + 1] + grid[y + 2][x + 2]):
                return False
            if t != (grid[y]    [x]     + grid[y + 1][x + 1] + grid[y + 2][x + 2]):
                return False
            if t != (grid[y + 2][x]     + grid[y + 1][x + 1] + grid[y]    [x + 2]):
                return False
            return True
        count = 0
        for x in range(xlen - 2):
            for y in range(ylen - 2):
                if is_magic_square(x, y):
                    count += 1
        return count
