class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int n = A.size();
        bool inc = true, dec = true;
        
        for (int i = 0; i < n - 1; i++) {
            if (A[i] > A[i + 1]) {
                inc = false;
            }
            if (A[i] < A[i + 1]) {
                dec = false;
            }
        }
        
        return inc || dec;
    }
};
