class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> jobs;
        for (int i = 0; i < difficulty.size(); i++) {
            jobs.push_back({profit[i], difficulty[i]});
        }
        
        sort(worker.rbegin(), worker.rend());
        sort(jobs.rbegin(), jobs.rend());
        
        int ans = 0;
        int widx = 0;
        for (auto &job: jobs) {
            int prof = job.first, diff = job.second;
            while (widx < worker.size() && worker[widx] >= diff) {
                ans += prof;
                widx++;
            }
            if (widx == worker.size()) break;
        }
        return ans;
    }
};
