class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int start, end;
        start = end = upper_bound(arr.begin(), arr.end(), x) - arr.begin();
        
        while (end - start < k) {
            if (start == 0) {
                end++;
            }
            else if (end == arr.size()) {
                start--;
            }
            else {
                if ((arr[end] - x) < (x - arr[start - 1])) {
                    end++;
                }
                else {
                    start--;
                }
            }
        }
        
        return vector<int>(arr.begin() + start, arr.begin() + end);
    }
};
