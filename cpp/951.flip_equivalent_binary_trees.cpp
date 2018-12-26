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
    bool dfs(TreeNode *t1, TreeNode *t2) {
        if (!t1 && !t2) return true;
        if (!t1 || !t2) return false;
        if (t1->val != t2->val) return false;
        
        if ((dfs(t1->left, t2->left) &&
             dfs(t1->right, t2->right)) ||
            (dfs(t1->left, t2->right) &&
             dfs(t1->right, t2->left))) {
            return true;
        }
        return false;
    }
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        return dfs(root1, root2);
    }
};
