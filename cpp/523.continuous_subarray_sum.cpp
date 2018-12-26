#include <iostream>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        deque<int> q;

        int n = nums.size();
        bool ret = false;

        for (int i = 2; i <= n; i++) {
            int sum = 0;
            for (int j = 0; j < i; j++) {
                sum += nums[j];
            }
            if (k == 0) {
                if (sum == 0) {
                    ret = true;
                    break;
                }
            }
            else if (sum % k == 0) {
                ret = true;
                break;
            }
            for (int j = i; j < n; j++) {
                sum -= nums[j - i];
                sum += nums[j];
                if (k == 0) {
                    if (sum == 0) {
                        ret = true;
                        break;
                    }
                }
                else if (sum % k == 0) {
                    ret = true;
                    break;
                }
            }
            if (ret) break;
        }
        return ret;
    }
};

int main() {
    Solution sol;

    vector<int> arr{23, 2, 4, 6, 7}; int k = 6;

    if (sol.checkSubarraySum(arr, k)) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
    return 0;
}
