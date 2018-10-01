class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xlen = len(grid)
        ylen = len(grid[0])
        
        cubes = 0
        touch = 0
        for x in range(xlen):
            for y in range(ylen):
                cubes += grid[x][y]
                if grid[x][y]:
                    touch += (grid[x][y] - 1) * 2
                if x + 1 < xlen:
                    touch += min(grid[x][y], grid[x + 1][y])
                if x - 1 >= 0:
                    touch += min(grid[x][y], grid[x - 1][y])
                if y + 1 < ylen:
                    touch += min(grid[x][y], grid[x][y + 1])
                if y - 1 >= 0:
                    touch += min(grid[x][y], grid[x][y - 1])
        return cubes * 6 - touch
