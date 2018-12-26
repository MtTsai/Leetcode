/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        queue<pair<TreeNode *, int>> q;
        if (!root) return true;

        q.push({root, 1});
        
        bool ret = true;
        int cur = 0;
        
        while (!q.empty()) {
            TreeNode *trie = q.front().first;
            int val = q.front().second;
            q.pop();
            
            
            if (val != cur + 1) {
                ret = false;
                break;
            }
            cur = val;

            if (trie->left) {
                q.push({trie->left, val * 2});
            }
            if (trie->right) {
                q.push({trie->right, val * 2 + 1});
            }
        }
        while (!q.empty()) q.pop();
        
        return ret;
    }
};
