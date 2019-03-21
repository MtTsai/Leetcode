class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        sort(A.begin(), A.end());
        
        int cur = -1;
        int moves = 0;
        
        for (auto i: A) {
            if (i > cur) {
                cur = i;
            }
            else {
                cur += 1;
                moves += cur - i;
            }
        }
        
        return moves;
    }
};
