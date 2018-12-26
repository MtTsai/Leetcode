class Solution {
public:
    vector<int> threeEqualParts(vector<int>& A) {
        int zcnt = 0;
        for (auto n: A) {
            if (n) zcnt++;
        }
        
        if (zcnt % 3 == 0) {
            if (zcnt == 0) {
                return {0, 2};
            }
            
            int s[3], ptr[3], idx = A.size() - 1;
            for (int i = 2; i >= 0; i--) {
                int cnt = 0;
                while (cnt < (zcnt / 3)) {
                    if (A[idx--]) cnt++;
                }
                s[i] = ptr[i] = idx + 1;
            }
            
            while (ptr[0] < s[1] &&
                   ptr[1] < s[2] &&
                   ptr[2] < A.size()) {
                if (A[ptr[0]] == A[ptr[1]] &&
                    A[ptr[0]] == A[ptr[2]]) {
                    ptr[0]++; ptr[1]++; ptr[2]++;
                    continue;
                }
                return {-1, -1};
            }
            if (ptr[2] == A.size() &&
                ptr[1] <= s[2] &&
                ptr[0] <= s[1]) {
                return {ptr[0] - 1, ptr[1]};
            }
        }        
        return {-1, -1};
    }
};
