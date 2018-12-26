class Solution {
public:
    string orderlyQueue(string S, int K) {
        if (K > 1) {
            sort(S.begin(), S.end());
        }
        else {
            string curS = S;
            for (int i = 0; i < S.size(); i++) {
                curS = curS.substr(1, curS.size() - 1) + curS.substr(0, 1);
                if (curS < S) {
                    S = curS;
                }
            }
        }

        return S;
    }
};
