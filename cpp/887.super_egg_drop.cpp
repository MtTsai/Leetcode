class Solution {
public:
    int superEggDrop(int K, int N) {
        vector<int> dp(K + 1); // means the max floor we can detect by i eggs by step s
        
        int step = 0;
        while (dp[K] < N) {
            step++;
            for (int i = K; i > 0; i--) {
                dp[i] = dp[i - 1] + dp[i] + 1;
            }
        }
        
        return step;
    }
};

#ifdef TLE_DFS_VER
class Solution {
public:
    int findn(int k, int n, vector<vector<int>> &dp) {
        if (dp[k][n] == 0) {
            if (k == 1) {
                dp[k][n] = n;
            }
            else if (n <= 2) {
                dp[k][n] = n;
            }
            else {
                dp[k][n] = n;
                for (int i = 2; i <= (n + 1) / 2; i++) {
                    int x = findn(k - 1, i - 1, dp);
                    int y = findn(k,     n - i, dp);
                    int t = max(x, y) + 1;
                    if (dp[k][n] < t) {
                        break;
                    }
                    dp[k][n] = t;
                }
                
            }
        }
        return dp[k][n];
    }
    int superEggDrop(int K, int N) {
        vector<vector<int>> dp(K + 1, vector<int>(N + 1, 0));
        
        return findn(K, N, dp);
    }
};
#endif
