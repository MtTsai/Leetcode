class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        priority_queue<int, vector<int>, greater<int>> xq;
        
        vector<pair<int, int>> ans;
        
        int curh = 0;
        
        for (auto b: buildings) {
            int li = b[0], ri = b[1], hi = b[2];
            
            while (!xq.empty() && xq.top() < li) {
                int x = xq.top();
                xq.pop();
                
                while (!q.empty() && q.top().second <= x) {
                    q.pop();
                }
                
                int h = (!q.empty()) ? -q.top().first : 0;
                if (curh != h) {
                    curh = h;
                    ans.push_back({x, h});
                }
            }
            
            xq.push(li);
            xq.push(ri);
            
            q.push({-hi, ri});
        }
        
        while (!xq.empty()) {
            int x = xq.top();
            xq.pop();

            while (!q.empty() && q.top().second <= x) {
                q.pop();
            }

            int h = (!q.empty()) ? -q.top().first : 0;
            if (curh != h) {
                curh = h;
                ans.push_back({x, h});
            }
        }
        
        return ans;
    }
    
    vector<pair<int, int>> getSkyline_tle2(vector<vector<int>>& buildings) {
        map<int, int> m;
        
        for (auto b: buildings) {
            int li = b[0], ri = b[1], hi = b[2];
            m[li] = m[ri] = 0;
        }
        
        for (auto b: buildings) {   
            int li = b[0], ri = b[1], hi = b[2];
            for (auto e = m.lower_bound(li); e != m.end(); e++) {
                int x = e->first, y = e->second;
                if (x >= ri) break;
                m[x] = max(m[x], hi);
            }
        }
        
        vector<pair<int, int>> ans;
        int cur = 0;
        for (auto &e: m) {
            int x = e.first, y = e.second;
            if (y != cur) {
                ans.push_back({x, y});
            }
            cur = y;
        }
        
        return ans;
    }
    
    vector<pair<int, int>> getSkyline_tle(vector<vector<int>>& buildings) {
        set<int> xset, yset;
        for (auto b: buildings) {
            int li = b[0], ri = b[1], hi = b[2];
            xset.insert(li);
            xset.insert(ri);
            
            yset.insert(hi);
        }
        
        vector<int> xarr, yarr;
        
        for (auto x: xset) xarr.push_back(x);
        for (auto y: yset) yarr.push_back(y);
        
        vector<vector<bool>> m(xarr.size(), vector<bool>(yarr.size(), false));
        
        for (auto b: buildings) {
            int li = b[0], ri = b[1], hi = b[2];
            for (int i = 0; i < xarr.size(); i++) {
                if (xarr[i] < li) continue;
                if (xarr[i] >= ri) break;
                
                for (int j = 0; j < yarr.size(); j++) {
                    if (yarr[j] > hi) break;
                    m[i][j] = true;
                }
            }
        }
        
        vector<pair<int, int>> ans;
        
        int cury = -1;
        for (int i = 0; i < xarr.size(); i++) {
            int j;
            // find highest position
            for (j = yarr.size() - 1; j >= 0; j--) {
                if (m[i][j]) break;
            }
            
            if (j != cury) {
                ans.push_back({xarr[i], (j >= 0) ? yarr[j] : 0});
            }
            cury = j;
        }
        
        return ans;
    }
};
