ass Solution {
public:
#define MOD ((int)(1e9 + 7))
    int knightDialer(int N) {
        vector<vector<int>> hops = {
            {4, 6},
            {6, 8},
            {7, 9},
            {4, 8},
            {3, 9, 0},
            {},
            {1, 7, 0},
            {2, 6},
            {1, 3},
            {2, 4}
        };
        
        vector<vector<int>> dp(10, vector<int>(N + 1, 0));
        
        for (int j = 0; j < 10; j++) {
            dp[j][0] = 1;
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < 10; j++) {
                for (auto hop: hops[j]) {
                    dp[j][i] = (dp[j][i] + dp[hop][i - 1]) % MOD;
                }
            }
        }
        
        int ans = 0;
        for (int j = 0; j < 10; j++) {
            ans = (ans + dp[j][N - 1]) % MOD;
        }
        
        return ans;
    }
};
