#include <iostream>
using namespace std;

class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2, int k) {

        if (k == 0) {
            if (nums1 == nums2) return 0;
            else return -1;
        }

        int n = nums1.size();
        long long a = 0, b = 0;

        for (int i = 0; i < n; i++) {
            long long diff = nums2[i] - nums1[i];
            if (abs(diff) % k != 0) return -1;
            if (diff > 0) {
                a += diff / k;
            } else {
                b += abs(diff) / k;
            }
        }

        // cout << a << "/" << b;
        if (a != b) return -1;
        return a;
    }
};
