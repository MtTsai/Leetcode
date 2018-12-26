#include <iostream>
#include <cstring>

using namespace std;

class Solution {
public:
    bool canTransform(string start, string end) {
        int sx = 0, ex = 0;
        int l = start.length();

        int si = 0, ei = 0;
        bool ret = false;

        while (true) {
            while (si < l && start[si] == 'X') si++;
            while (ei < l && end[ei] == 'X') ei++;

            ret = (si == l && ei == l);

            if (si == l || ei == l) {
                break;
            }
            if (start[si] != end[ei]) {
                break;
            }
            if (start[si] == 'R' && si > ei) break;
            if (start[si] == 'L' && si < ei) break;
            si++; ei++;
        }
        return ret;
    }
};

int main() {
    Solution sol;
    string s = "RXXLRXRXL";
    string e = "XRLXXRRLX";

    cout << sol.canTransform(s, e);

    return 0;
}
