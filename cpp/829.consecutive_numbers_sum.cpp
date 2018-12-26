/* example for the rule:
 *
 *     4 Num's sum:
 *         1 + 2 + 3 + 4 = 10
 *         2 + 3 + 4 + 5 = 14
 *         ....
 *         4x + 10 = 4n + 6
 *
 *
 *     So the Num's sum will be:
 *         n,
 *         2n + 1,
 *         3n + 3, 4n + 6, 5n + 10, 6n + 15 ...
 *
 *     evaluate the maximum Num:
 *         (1 + n) * n / 2 = N
 *         n ~< sqrt (N * 2)
 */


class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int ans = 0;
        int round = sqrt(N * 2);
        for (int i = 0; i < round; i++) {
            N -= i;
            if (N % (i + 1)) continue;
            ans++;
        }
        return ans;
    }
};
