class Solution {
public:
    int _gcd(int x, int y) {
        while (y) {
            x %= y;
            swap(x, y);
        }
        return x;
    }
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();        
        
        if (n != 0 && k != 0) {
            k %= n;
            int gcd = _gcd(n, k);
            
            for (int i = 0; i < gcd; i++) {
                int j = i;
                while ((j = (j - k + n) % n) != i) {
                    swap(nums[j], nums[(j + k) % n]);
                }
            }
        }
    }
};
