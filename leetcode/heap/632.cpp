// #include <queue>
// #include <set>

// class Solution {
// public:
//     vector<int> smallestRange(vector<vector<int>>& nums) {
//         // non-decreasing order
//         // smallest range 
//         // prefix approach?
//         // sorted.

//         // [4,10,15,24,26]
//         // [0,9,12,20],
//         // [5,18,22,30]

//         vector<int> ans(2);

//         int k = nums.size();

//         vector<int> indices(k, 0);
//         multiset<int> values;
//         priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

//         for (int i = 0; i < k; i++) {
//             pq.push({nums[i][0], i});
//             values.insert(nums[i][0]);
//         }
        
//         ans[0] = *values.begin();
//         ans[1] = *values.rbegin();

//         while (!pq.empty()) {
//             auto [value, index] = pq.top();
//             pq.pop();

//             indices[index]++;
//             if (indices[index] >= nums[index].size())
//                 break;

//             int new_value = nums[index][indices[index]];

//             // remove one element
//             auto it = values.find(value);
//             if (it != values.end()) values.erase(it);

//             values.insert(new_value);
//             pq.push({new_value, index});

//             int min = *values.begin();
//             int max = *values.rbegin();
//             if (ans[1] - ans[0] > max - min) {
//                 ans[0] = min, ans[1] = max;
//             }
//         }
    
//         return ans;
//     }
// };

#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        using T = tuple<int, int, int>; 
        // {value, listIndex, elemIndex}

        priority_queue<T, vector<T>, greater<T>> pq;

        int currentMax = INT_MIN;

        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i][0], i, 0});
            currentMax = max(currentMax, nums[i][0]);
        }

        int bestL = get<0>(pq.top());
        int bestR = currentMax;

        while (true) {
            auto [currentMin, listIdx, elemIdx] = pq.top();
            pq.pop();

            if ((bestR - bestL > currentMax - currentMin) ||
                (bestR - bestL == currentMax - currentMin && currentMin < bestL)) {
                bestL = currentMin;
                bestR = currentMax;
            }

            if (elemIdx + 1 == nums[listIdx].size()) {
                break;
            }

            int nextVal = nums[listIdx][elemIdx + 1];
            pq.push({nextVal, listIdx, elemIdx + 1});
            currentMax = max(currentMax, nextVal);
        }

        return {bestL, bestR};
    }
};
