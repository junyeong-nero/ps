#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int solution(vector<vector<int>> visible, vector<vector<int>> hidden, int K) {
    int N = visible.size();
    int M = visible[0].size();

    const int INF = 1e9;
    int answer = INT_MIN;

    for (int mask = 0; mask < (1 << N); mask++) {
        int rowCost = __builtin_popcount((unsigned)mask) * K;

        // colSum[j][b]:
        //   j번째 열을 b(0: 유지, 1: 뒤집기) 했을 때 해당 열의 총합
        //   b == 1이면 열 뒤집기 비용 K 포함
        //
        // oddMin[j][b]:
        //   j번째 열을 b로 선택했을 때,
        //   (i+j)%2==1 인 칸들 중 최소값
        vector<vector<int>> colSum(M, vector<int>(2, 0));
        vector<vector<int>> oddMin(M, vector<int>(2, INF));

        for (int j = 0; j < M; j++) {
            for (int b = 0; b <= 1; b++) {
                int sum = (b ? -K : 0);
                int mn = INF;

                for (int i = 0; i < N; i++) {
                    bool rowFlip = ((mask >> i) & 1);
                    bool flipped = rowFlip ^ b;

                    int val = flipped ? hidden[i][j] : visible[i][j];
                    sum += val;

                    if ((i + j) % 2 == 1) {
                        mn = min(mn, val);
                    }
                }

                colSum[j][b] = sum;
                oddMin[j][b] = mn;
            }
        }

        // 둘 중 하나라도 홀수면 min_value를 뺄 필요가 없음
        if ((N % 2 == 1) || (M % 2 == 1)) {
            int total = -rowCost;
            for (int j = 0; j < M; j++) {
                total += max(colSum[j][0], colSum[j][1]);
            }
            answer = max(answer, total);
            continue;
        }

        // N, M이 둘 다 짝수면
        // 전체 odd parity 칸들 중 최소값 하나를 빼야 함
        //
        // 어떤 (pivotCol, pivotFlip)이 전역 odd minimum을 담당한다고 고정하고 계산
        int bestForMask = INT_MIN;

        for (int pivotCol = 0; pivotCol < M; pivotCol++) {
            for (int pivotFlip = 0; pivotFlip <= 1; pivotFlip++) {
                int t = oddMin[pivotCol][pivotFlip];
                if (t == INF) continue;

                int total = -rowCost;
                bool ok = true;

                for (int j = 0; j < M; j++) {
                    if (j == pivotCol) {
                        total += colSum[j][pivotFlip];
                        continue;
                    }

                    int best = INT_MIN;

                    // 열 j를 안 뒤집는 경우
                    if (oddMin[j][0] >= t) {
                        best = max(best, colSum[j][0]);
                    }

                    // 열 j를 뒤집는 경우
                    if (oddMin[j][1] >= t) {
                        best = max(best, colSum[j][1]);
                    }

                    if (best == INT_MIN) {
                        ok = false;
                        break;
                    }

                    total += best;
                }

                if (!ok) continue;

                total -= t;
                bestForMask = max(bestForMask, total);
            }
        }

        answer = max(answer, bestForMask);
    }

    return answer;
}

// #include <string>
// #include <vector>
// #include <iostream>

// using namespace std;

// int N, M, K;
// vector<vector<int>> V;
// vector<vector<int>> H;

// int dfs(int index, int row_flip, int col_flip) {
//     int T = min(N, M);
//     if (index == T) {
        
//         int res = 0;
//         int min_value = 1e9;
        
//         for (int x = 0; x < T; x++) {
//             for (int y = 0; y < T; y++) {
                
//                 int flip = 0;
//                 if ((row_flip >> x) & 1) flip++;
//                 if ((col_flip >> y) & 1) flip++;
                
//                 int value = V[x][y];
//                 if (flip & 1) 
//                     value = H[x][y];
                
//                 if (!((x == 0 && y == 0) || (x == T - 1 && y == T - 1)))
//                     min_value = min(min_value, value);
                
//                 res += value;
//             }
//         }
        
//         if (T % 2 == 0)
//             res -= min_value;
        
//         cout << res << endl;
        
//         for (int x = 0; x < T; x++)
//             if ((row_flip >> x) & 1) res -= K;
        
//         for (int y = 0; y < T; y++)
//             if ((col_flip >> y) & 1) res -= K;
        
//         return res;
//     }
    
//     int res = 0; 
//     int target = 1 << index;
//     res = max(res, dfs(index + 1, row_flip, col_flip));
//     res = max(res, dfs(index + 1, row_flip | target, col_flip));
//     res = max(res, dfs(index + 1, row_flip, col_flip | target));
//     res = max(res, dfs(index + 1, row_flip | target, col_flip | target));
    
//     return res;
// }


// int solution(vector<vector<int>> visible, vector<vector<int>> hidden, int k) {
    
//     V = visible, H = hidden, K = k;
//     N = visible.size();
//     M = visible[0].size();
    
//     int answer = dfs(0, 0, 0);
//     return answer;
// }
