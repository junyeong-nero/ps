
class Solution {
public:
    long long check(int h, vector<int>& beans) {
        long long res = 0;
        for (auto bean : beans) {
            if (bean >= h) {
                res += bean - h;
            } else {
                res += bean;
            }
        }
        return res;
    }

    long long minimumRemoval(vector<int>& beans) {

        int n = beans.size();
        sort(beans.begin(), beans.end());

        long long total = 0;
        for (auto bean : beans)
            total += bean;

        long long res = 1e12;
        for (long long i = 0; i < n; i++) {
            res = min(res, total - (n - i) * beans[i]);
        }

        return res;

        // int left = *min_element(beans.begin(), beans.end());
        // int right = *max_element(beans.begin(), beans.end());

        // while (left <= right) {
        //     int mid = left + (right - left) / 2;
        //     if (check(mid, beans) < check(mid + 1, beans)) {
        //         right = mid - 1;
        //     } else {
        //         left = mid + 1;
        //     }
        // }

        // return check(left, beans);
    }
};
