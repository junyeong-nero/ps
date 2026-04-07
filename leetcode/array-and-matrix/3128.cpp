class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        
        vector<long> row_counter(n);
        vector<long> col_counter(m);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row_counter[j] += grid[i][j];
                col_counter[i] += grid[i][j];
            }
        }

        long long res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    res += (col_counter[i] - 1) * (row_counter[j] - 1);
                }
            }
        }

        return res;
    }
};
