class Solution {
public:
    const int mod = 1e9 + 7;
    long long power(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1)
                res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }

    long long modInv(long long n) { return power(n, mod - 2); }

    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int limit = sqrt(n);

        // group queries with small k for later processing
        unordered_map<int, vector<vector<int>>> lightK;

        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            if (k >= limit) { // large k: apply brute force
                for (int i = l; i <= r; i += k)
                    nums[i] = (1LL * nums[i] * v) % mod;
            } else { // small k: process later
                lightK[k].push_back(q);
            }
        }

        for (auto& [k, query] : lightK) {
            // process small queries grouped by step size k
            vector<long long> diff(n, 1);
            for (auto& q : query) {
                int l = q[0], r = q[1], v = q[3];
                // multiply starting position
                diff[l] = (diff[l] * v) % mod;
                // cancel the multiplication using modular inverse
                int steps = (r - l) / k;
                int next = l + (steps + 1) * k;
                if (next < n) {
                    diff[next] = (diff[next] * modInv(v)) % mod;
                }
            }

            // propagate the multipliers with a step size of k
            for (int i = 0; i < n; i++) {
                if (i >= k)
                    diff[i] = (diff[i] * diff[i - k]) % mod;
                nums[i] = (1LL * nums[i] * diff[i]) % mod;
            }
        }

        int ans = 0;
        for (auto& num : nums)
            ans ^= num;

        return ans;
    }
};

// class Solution {
// public:
//     int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {

//         // n = 10^5
//         // solve within O(n log n)

//         int MOD = 1e9 + 7;
//         int n = nums.size();
//         int m = queries.size();

//         // sort queries.
//         sort(queries.begin(), queries.end());
//         int query_index = 0;
//         int res = 0;

//         for (int i = 0; i < n; i++) {

//             while (query_index < m && queries[query_index][1] < i)
//                 query_index++;

//             for (int j = query_index; j < m; j++) {

//                 int L = queries[j][0];
//                 int R = queries[j][1];
//                 int K = queries[j][2];
//                 int V = queries[j][3];

//                 if (L <= i && i <= R) {
//                     if ((i - L) % K == 0) {
//                         nums[i] = ((long)nums[i] * V) % MOD;
//                     }
//                 } else {
//                     break;
//                 }
//             }

//             res ^= nums[i];
//         }
//         return res;
//     }
// };
