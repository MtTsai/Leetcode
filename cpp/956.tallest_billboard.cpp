class Solution {
    int sum;
public:
    int dfs(int d, int base, int diff, vector<int> &rods, vector<vector<int>> &dp) {        
        if (dp[d][diff] > -5001) return dp[d][diff];

        int ret = (diff == 0) ? 0 : sum * -1;

        if (d < rods.size()) {
            // ret = max(ret,  dp[d + 1][new diff] + (new base - cur base))

            ret = max(ret, dfs(d + 1, base, diff, rods, dp));
            
            ret = max(ret, dfs(d + 1, base, diff + rods[d], rods, dp));
            
            if (diff > rods[d]) {
                ret = max(ret, dfs(d + 1, base + rods[d], diff - rods[d], rods, dp) + rods[d]);
            }
            else {
                ret = max(ret, dfs(d + 1, base + diff, rods[d] - diff, rods, dp) + diff);                
            }
        }
        dp[d][diff] = ret;
        
        return ret;
    }
    int tallestBillboard(vector<int>& rods) {
        if (rods.size() < 2) return 0;
        
        sum = 0;
        for (int i = 0; i < rods.size(); i++) {
            sum += rods[i];
        }

        // d[i][j] denotes the tallest value with 0 base
        //      when
        //          start from i-th rod
        //          diff j between left and right
        vector<vector<int>> dp(rods.size() + 1, vector<int>(sum + 1, -5001));
        
        dfs(0, 0, 0, rods, dp);
        
        return dp[0][0];
    }
};
