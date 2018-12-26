struct data {
    int x;
    int y;
    int l;
};
class Solution {
public:

    int cutOffTree(vector<vector<int>>& forest) {
        int r = forest.size();
        int c = forest[0].size();
        vector<pair<int, int>>order;
        vector<vector<int>> dp(r, vector<int>(c, -1));
#define X(n) (n / c)
#define Y(n) (n % c)
#define POS(x, y) ((x) * c + (y))
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int v = forest[i][j];
                if (v > 0) {
                    order.push_back({v, POS(i, j)});
                }
            }
        }
        
        sort(order.begin(), order.end());
        int cnt = order.size();
        int cx = 0, cy = 0;
        int step = 0;
        queue<data> q;
        for (int i = 0; i < cnt; i++) {
            q.push({X(order[i].second), Y(order[i].second), 0});
            
            int move = -1;
            while (!q.empty()) {
                int x = q.front().x, y = q.front().y, l = q.front().l; q.pop();
                if (x == cx && y == cy) {
                    move = l;
                    break;
                }
                if (dp[x][y] == i) continue;
                
                dp[x][y] = i;
                
                if (forest[x][y] == 0) continue;
                
                if (x > 0)     q.push({x - 1, y, l + 1});
                if (x < r - 1) q.push({x + 1, y, l + 1});
                if (y > 0)     q.push({x, y - 1, l + 1});
                if (y < c - 1) q.push({x, y + 1, l + 1});
            }
            while (!q.empty()) q.pop();
            
            if (move < 0) {
                return -1;
            }
            step += move;
            cx = X(order[i].second); cy = Y(order[i].second);
        }
        return step;
    }
};
