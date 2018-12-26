#include <vector>
#include <utility>

using namespace std;

class MyCalendarThree {
public:
    MyCalendarThree() {
    }

    int find(int x) {
        int l = 0, r = t.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (t[mid].first >= x) {
                r = mid;
            }
            else {
                l = mid + 1;
            }
        }
        return l;
    }
    
    vector<pair<int, int>>::iterator vfind(int x) {
        return lower_bound(t.begin(), t.end(), make_pair(x, 0));
    }

    int vbook(int start, int end) {
        vector<pair<int, int>>::iterator pos = vfind(start);
        if (pos != t.end() && pos->first == start) {
            pos->second += 1;
        }
        else {
            t.insert(pos, {start, 1});
        }
        pos = vfind(end);
        if (pos != t.end() && pos->first == end) {
            pos->second -= 1;
        }
        else {
            t.insert(pos, {end, -1});
        }
        return ans();
    }
    
    int ans(void) {
        int cnt = 0;
        int a = 0;
        for (int i = 0; i < t.size(); i++) {
            cnt += t[i].second;
            a = (a > cnt) ? a : cnt;
        }
        return a;
    }
    
    int book(int start, int end) {
        return vbook(start, end);
        int pos = find(start);
        if (pos < t.size() && t[pos].first == start) {
            t[pos].second += 1;
        }
        else {
            t.insert(t.begin() + pos, {start, 1});
        }
        pos = find(end);
        if (pos < t.size() && t[pos].first == end) {
            t[pos].second -= 1;
        }
        else {
            t.insert(t.begin() + pos, {end, -1});
        }

        return ans();
    }
private:
    vector<pair<int, int>> t;
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */

int main() {
    return 0;
}
