#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int row, col, area;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        area = 0;
        row = grid.size();
        col = grid[0].size();

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    int t = 0;
                    dfs(i, j, grid, t);
                    area = (area > t) ? area : t;
                }
            }
        }

        return area;
    }

    void dfs(int x, int y, vector<vector<int>>& grid, int &t) {
        if (grid[x][y]) {
            t += 1;
            grid[x][y] = 0;
            if (x > 0)       dfs(x - 1, y, grid, t);
            if (x < row - 1) dfs(x + 1, y, grid, t);
            if (y > 0)       dfs(x, y - 1, grid, t);
            if (y < col - 1) dfs(x, y + 1, grid, t);
        }
    }
};


int main() {
    Solution sol;

    vector<vector<int>> grid = {
       {0,0,1,0,0,0,0,1,0,0,0,0,0},
       {0,0,0,0,0,0,0,1,1,1,0,0,0},
       {0,1,1,0,1,0,0,0,0,0,0,0,0},
       {0,1,0,0,1,1,0,0,1,0,1,0,0},
       {0,1,0,0,1,1,0,0,1,1,1,0,0},
       {0,0,0,0,0,0,0,0,0,0,1,0,0},
       {0,0,0,0,0,0,0,1,1,1,0,0,0},
       {0,0,0,0,0,0,0,1,1,0,0,0,0}
    };
    cout << sol.maxAreaOfIsland(grid) << endl;
    
    return 0;
}

