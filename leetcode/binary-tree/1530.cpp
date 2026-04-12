
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int res = 0;
    
    vector<int> dfs(TreeNode* cur, int distance) {
        if (cur == nullptr)
            return {};
        if (cur->left == nullptr && cur->right == nullptr)
            return {1};

        vector<int> L = dfs(cur->left, distance);
        vector<int> R = dfs(cur->right, distance);

        for (auto left : L) {
            for (auto right : R) {
                if (left + right <= distance) {
                    res++;
                }
            }
        }

        vector<int> v;
        for (auto elem : L) v.push_back(elem + 1);
        for (auto elem : R) v.push_back(elem + 1);
        return v;
    }

    int countPairs(TreeNode* root, int distance) {
        dfs(root, distance);
        return res;
    }
};
