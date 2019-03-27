class Solution {
public:
    int numDupDigitsAtMostN(int N) {
        vector<int> num;
        int n_ori = N;
        
        // Transform N + 1 to list
        N += 1;
        while (N) {
            num.insert(num.begin(), N % 10);
            N /= 10;
        }
        
        int no_repeat = 0;
        
        // e.g. 3435 + 1 = 3436
        // 1 ~ 9
        // 1X ~ 9X
        // 1XX ~ 9XX
        for (int i = 1; i < num.size(); i++) {
            int t = 9;
            for (int j = 1; i + j < num.size(); j++) {
                t *= 10 - j;
            }
            no_repeat += t;
        }
        
        // 1XXX ~ 2XXX
        // 30XX ~ 33XX
        // 340X ~ 342X
        // 3430 ~ 3435
        int bitmap = 0;
        for (int p = 0; p < num.size(); p++) {
            for (int i = (p == 0); i < num[p]; i++) {
                // skip repeated
                if ((1 << i) & bitmap) continue;
                
                int t = 1;
                for (int j = p + 1; j < num.size(); j++) {
                    t *= 10 - j;
                }
                no_repeat += t;
            }
            // leading digits repeated, break the loop
            if ((1 << num[p]) & bitmap) break;
            bitmap |= (1 << num[p]);
        }
        
        return n_ori - no_repeat;
    }
};
