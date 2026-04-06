class Solution {
public:
    long long dfs(TreeNode* root, vector<long long>& value) {
        if (root == nullptr) return 0;

        long long res = root->val;
        res += dfs(root->left, value);
        res += dfs(root->right, value);

        value.push_back(res);
        return res;
    }

    int maxProduct(TreeNode* root) {
        const int MOD = 1e9 + 7;
        vector<long long> value;

        long long total = dfs(root, value);

        sort(value.begin(), value.end());

        auto it = upper_bound(value.begin(), value.end(), total / 2);

        long long best = 0;

        if (it != value.end()) {
            long long x = *it;
            best = max(best, x * (total - x));
        }

        if (it != value.begin()) {
            --it;
            long long x = *it;
            best = max(best, x * (total - x));
        }

        return best % MOD;
    }
};
