class Solution {
public:
    long long find(long long x, long long target, unordered_map<long long, long long>& m) {
        if (target == 0) {
            return 0;
        }
        
        if (target < x) {
            return min(// + x/x + x/x + ...
                       target * 2 - 1,
                       // + x - x/x - x/x - x/x
                       (x - target) * 2
                   );
        }
        else {
            bool first = !m.count(target);
            if (first || m[target] == target * 2) {
                m[target] = target * 2;

                int d = 0, n = x;
                while (n * x <= target) {
                    d++;
                    n *= x;
                }
                if (n == target) {
                    m[target] = d;
                }
                else {
                    if (first || !m.count(n * x - target)) {
                        m[target] = min(m[target], d + 2 + find(x, n * x - target, m));
                    }
                    if (first || !m.count(target - n)) {
                        m[target] = min(m[target], d + 1 + find(x, target - n, m));
                    }
                }
            }
            return m[target];
        }
    }
    int leastOpsExpressTarget(int x, int target) {
        unordered_map<long long, long long> m;
        return find(x, target, m);
    }
};
