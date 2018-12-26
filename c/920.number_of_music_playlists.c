int numMusicPlaylists(int N, int L, int K) {
    int mod = 1000000007;
    int n, l;
    int *dp = (int *)malloc(sizeof(int) * (N + 1) * (L + 1));
    int ans = 0;
    
    memset(dp, 0, sizeof(int) * (N + 1) * (L + 1));

#define DP(x, y) (dp[((x) * (L + 1)) + y])
    
    for (n = 0; n <= N; n++) {
        for (l = 0; l <= L; l++) {
            long long int t = 0;
            if (n == 0 && l == 0) {
                t = 1;
            }
            else if (n == 0 || l == 0) {
                t = 0;
            }
            else {
                t = ((long long int)DP(n - 1, l - 1) * (N - (n - 1))) % mod;
                if (n > K) {
                    t = (t + ((long long int)DP(n, l -1)) * (n - K)) % mod;
                }
            }
            DP(n, l) = t;
        }
    }
    
    ans = DP(N, L);
    free(dp);
    return ans;
}
