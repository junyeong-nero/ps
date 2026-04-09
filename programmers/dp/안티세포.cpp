#include <vector>
#include <algorithm>
using namespace std;

static const int MOD = 1'000'000'007;

vector<int> solution(vector<int> a, vector<int> s) {
    vector<int> answer;
    int offset = 0;

    for (int len : s) {
        vector<long long> b(len + 1); // 1-based
        for (int i = 1; i <= len; ++i) {
            b[i] = a[offset + i - 1];
        }
        offset += len;

        // good[r] = { (sum, start) ... }
        // r에서 끝나는 "완전히 합성 가능한 구간"들을
        // sum 오름차순(= 매번 2배씩 증가)으로 저장
        vector<vector<pair<long long, int>>> good(len + 1);

        vector<int> dp(len + 1, 0);
        dp[0] = 1;

        for (int r = 1; r <= len; ++r) {
            long long curSum = b[r];
            int curStart = r;

            int ways = 0;
            vector<pair<long long, int>> chain;

            while (true) {
                chain.push_back({curSum, curStart});
                ways += dp[curStart - 1];
                if (ways >= MOD) ways -= MOD;

                if (curStart == 1) break;

                const auto& prevList = good[curStart - 1];

                auto it = lower_bound(
                    prevList.begin(), prevList.end(),
                    make_pair(curSum, -1),
                    [](const pair<long long, int>& x, const pair<long long, int>& y) {
                        return x.first < y.first;
                    }
                );

                if (it == prevList.end() || it->first != curSum) {
                    break;
                }

                curStart = it->second;
                curSum <<= 1; // 2배
            }

            good[r] = move(chain);
            dp[r] = ways;
        }

        answer.push_back(dp[len]);
    }

    return answer;
}
