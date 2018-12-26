class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int h = grid.size(), w = grid[0].size();
        
        vector<vector<int>> m(h * 3, vector<int>(w * 3, 0));
        
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                char t = grid[i][j];
                if (t == '/') {
                    m[i * 3][j * 3 + 2] = \
                    m[i * 3 + 1][j * 3 + 1] = \
                    m[i * 3 + 2][j * 3] = 1;
                }
                if (t == '\\') {
                    m[i * 3][j * 3] = \
                    m[i * 3 + 1][j * 3 + 1] = \
                    m[i * 3 + 2][j * 3 + 2] = 1;
                }
            }
        }
        
        int cnt = 0;
        for (int i = 0; i < h * 3; i++) {
            for (int j = 0; j < w * 3; j++) {
                if (m[i][j]) continue;
                
                // a new empty place
                cnt++;
                queue<pair<int, int>> q;
                q.push({i, j});
                while (!q.empty()) {
                    int y = q.front().first, x = q.front().second;
                    q.pop();
                    if (m[y][x]) continue;
                    m[y][x] = 1;
                    if (y > 0)         q.push({y - 1, x});
                    if (y < h * 3 - 1) q.push({y + 1, x});
                    if (x > 0)         q.push({y, x - 1});
                    if (x < w * 3 - 1) q.push({y, x + 1});
                }
            }
        }
        return cnt;
    }
};
