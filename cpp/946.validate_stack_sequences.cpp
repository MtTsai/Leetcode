class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        deque<int> q;
        int l = pushed.size();
        
        int i = 0, j = 0;
        
        while (i < l) {
            q.push_back(pushed[i]);
            i++;
            
            while (!q.empty() && q.back() == popped[j]) {
                j++;
                q.pop_back();
            }            
        }
        
        return (j == l);
    }
};
