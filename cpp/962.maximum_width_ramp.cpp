class Solution {
public:
    int maxWidthRamp(vector<int>& A) {
        vector<int> postmax(A);
        
        for (int i = A.size() - 2; i >= 0; i--) {
            postmax[i] = max(postmax[i], postmax[i + 1]);
        }
        
        int ans = 0;
        
        queue<int> q;
        
        for (int i = 0; i < A.size(); i++) {
            q.push(i);
            
            while (A[q.front()] > postmax[i]) {
                q.pop();
            }
            
            ans = max(ans, i - q.front());
        }
        return ans;
    }
};
