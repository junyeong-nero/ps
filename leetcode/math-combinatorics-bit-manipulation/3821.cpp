class Solution {
public:
    long long nthSmallest(long long n, int k) {
        // arr[d] = d자리 수 중 1이 정확히 k개인 수의 개수
        //        = C(d - 1, k - 1)
        vector<long long> arr(55, 0);
        vector<long long> prefix(55, 0);

        // 조합 미리 계산
        vector<vector<long long>> comb(55, vector<long long>(55, 0));
        for (int i = 0; i < 55; i++) {
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
            }
        }

        for (int d = k; d < 55; d++) {
            arr[d] = comb[d - 1][k - 1];
        }

        for (int d = 1; d < 55; d++) {
            prefix[d] = prefix[d - 1] + arr[d];
        }

        // 1) n번째 수의 자리수 찾기
        int digit = lower_bound(prefix.begin(), prefix.end(), n) - prefix.begin();

        // 2) digit자리 수들 중 몇 번째인지
        n -= prefix[digit - 1];

        long long ans = 0;

        // 맨 앞자리는 무조건 1
        ans |= (1LL << (digit - 1));

        int remainOne = k - 1;      // 앞으로 더 채워야 하는 1 개수
        int remainPos = digit - 1;  // 현재 뒤에 남은 자리 수

        // 3) 나머지 자리를 하나씩 결정
        for (int pos = digit - 2; pos >= 0; pos--) {
            if (remainOne == 0) break;

            // 현재 자리를 0으로 두면
            // 남은 remainPos - 1 자리에서 remainOne 개를 골라야 함
            long long zeroBlock = 0;
            if (remainPos - 1 >= remainOne) {
                zeroBlock = comb[remainPos - 1][remainOne];
            }

            if (n <= zeroBlock) {
                // 현재 자리는 0
            } else {
                // 현재 자리는 1
                n -= zeroBlock;
                ans |= (1LL << pos);
                remainOne--;
            }

            remainPos--;
        }

        return ans;
    }
};
