class Solution {
public:
    void classify(vector<int> &ans, int start, int len) {
        if (len <= 1) return;
        int m = (len + 1) / 2;
        {
            vector<int> tmp(ans.begin() + start, ans.begin() + start + len);
            for (int i = 0; i < m; i++) {
                ans[start + i] = tmp[i * 2];
            }
            for (int i = m; i < len; i++) {
                ans[start + i] = tmp[(i - m) * 2 + 1];
            }
        }
        
        classify(ans, start, m);
        classify(ans, start + m, len - m);
    }
    vector<int> beautifulArray(int N) {
        vector<int> ans;
        for (int i = 1; i <= N; i++) ans.push_back(i);
        
        classify(ans, 0, N);
        
        return ans;
    }
};
