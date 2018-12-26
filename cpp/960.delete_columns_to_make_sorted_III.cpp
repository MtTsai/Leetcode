class Solution {
public:
    int minDeletionSize(vector<string>& A) {
        int slen = A[0].size();
        vector<int> dp(slen, 1); /* means max valid columns in string [0..i] */
        
        for (int i = 1; i < slen; i++) {
            for (int j = 0; j < i; j++) {
                bool match = true;
                for (auto s: A) {
                    if (s[j] > s[i]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        return slen - (*(max_element(dp.begin(), dp.end())));
    }
};
