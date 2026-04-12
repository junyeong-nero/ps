class Solution {
public:

    int INF = 1e9;

    int dist(pair<int,int>& pos1, pair<int,int>& pos2) {
        return abs(pos1.first - pos2.first) + abs(pos1.second - pos2.second);
    }

    pair<int,int> get_pos(char c) {
        int index = c - 'A';
        int x = index / 6;
        int y = index % 6;
        return {x, y};
    }

    int get_dist(char a, char b) {
        auto pa = get_pos(a);
        auto pb = get_pos(b);
        return dist(pa, pb);
    }

    int minimumDistance(string word) {
        // two fingers?
        // for (int i = 0; i < 26; i++) {
        //     char c = i + 'A';
        //     auto [x, y] = get_pos(c);
        //     cout << c << ": " <<  x << ", " << y << endl;
        // }

        vector<vector<int>> dp(26, vector<int>(26, 0));
        // dp[left][right] : minimum distance at left, right;

        for (int i = 0; i < word.size(); i++) {

            char cur = word[i];
            int cur_idx = word[i] - 'A';

            vector<vector<int>> new_dp(26, vector<int>(26, INF)); 
            for (int left = 0; left < 26; left++) {
                for (int right = 0; right < 26; right++) {
                    new_dp[cur_idx][right] = min(new_dp[cur_idx][right], get_dist(left + 'A', cur) + dp[left][right]);
                    new_dp[left][cur_idx] = min(new_dp[left][cur_idx], get_dist(right + 'A', cur) + dp[left][right]);
                }
            }

            dp = new_dp;
        }

        int res = INF;
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++)
                res = min(res, dp[i][j]);

        return res;
    }
};
