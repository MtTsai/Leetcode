class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        unordered_set<string> str_set;
        queue<tuple<string, int, int>> q;
        
        string target = "";
        
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 3; j++) {
                target += (char)(board[i][j] + '0');
            }
        }
        
        q.push(make_tuple("123450", 5, 0));
        
        vector<vector<int>> next = {{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};
        
        int ans = -1;
        while (!q.empty()) {
            string s = get<0>(q.front());
            int pos  = get<1>(q.front());
            int step = get<2>(q.front());
            q.pop();
            
            if (s == target) {
                ans = step;
                break;
            }
            
            if (str_set.count(s)) {
                continue;
            }
            str_set.insert(s);
            
            for (auto _next: next[pos]) {
                string _s = s;
                swap(_s[_next], _s[pos]);
                q.push(make_tuple(_s, _next, step + 1));
            }
        }
        
        while (!q.empty()) q.pop();
        
        return ans;
    }
};
