class Solution {
public:
    bool is_same(vector<int> &a, vector<int> &b) {
        for (int i = 0; i < 8; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
    vector<int> prisonAfterNDays(vector<int>&c, int N) {
        queue<vector<int>> q;
        vector<int> cells(c);
        
        for (int day = 1; day <= N; day++) {
            vector<int> old_cells(cells);
            
            cells[0] = cells[7] = 0;
            for (int i = 1; i < 7; i++) {
                cells[i] = (old_cells[i - 1] == old_cells[i + 1]) ? 1 : 0;
            }
            if (day == 64) {
                while (!is_same(q.front(), cells)) q.pop();
                
                int remain = (N - day) % q.size();
                while (remain--) q.pop();
                
                cells = q.front();
                break;
            }
            q.push(cells);
        }
        while (!q.empty()) q.pop();
        
        return cells;
    }
};
