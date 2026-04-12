class Solution {
public:
    int uniqueXorTriplets(vector<int>& a) {
        unordered_set<int> st, s;
        int n = a.size();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                st.insert(a[i] ^ a[j]);
            }
        }

        for (auto num : st) {
            for (auto x : a) {     // num = a[i] ^ a[j] (XOR of pairs)
                s.insert(num ^ x); // num^x = a[i]^a[j]^a[k]  ---> triplet xor
                                   // inserted in set s for uniqueness
            }
        }
        return s.size();
    }
};
