class Solution {
public:
    int maxEnvelopes(vector<pair<int, int>>& e) {
        if (e.size() == 0) return 0;
        
        sort(e.begin(), e.end());
        
        vector<int> cnt(e.size(), 1);
        
        for (int i = 0; i < e.size() - 1; i++) {
            for (int j = i + 1; j < e.size(); j++) {
                if (e[i].first  < e[j].first &&
                    e[i].second < e[j].second) {
                    cnt[j] = max(cnt[j], cnt[i] + 1);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < e.size(); i++)
            ans = max(ans, cnt[i]);
        return ans;
    }
};

//// TLE version
class Solution {
    map<int, vector<pair<int, int>>> m;
    vector<int> worder;
    int ans;
public:
    int dfs(int w_ord, int cur_h) {
        int ret = 0;
        if (w_ord < worder.size()) {
            int w = worder[w_ord];
            // take one h in the w list
            for (int i = 0; i < m[w].size(); i++) {
                int h = m[w][i].first;
                if (h > cur_h) {
                    if (m[w][i].second < 0) {
                        m[w][i].second = dfs(w_ord + 1, h) + 1;
                    }
                    ret = max(ret, m[w][i].second);
                }
            }
            
            // not take
            ret = max(ret, dfs(w_ord + 1, cur_h));
        }
        ans = max(ans, ret);
        return ret;
    }
    
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        for (int i = 0; i < envelopes.size(); i++) {
            int w = envelopes[i].first, h = envelopes[i].second;
            m[w].push_back({h, -1});
        }
        for (auto &m_it: m) {
            worder.push_back(m_it.first);
        }
        if (worder.size() == 0) return 0;
        
        dfs(0, 0);
        return ans;
    }
};
