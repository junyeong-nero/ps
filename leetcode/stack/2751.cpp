#include <algorithm>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {

        // size with vector<int>&
        int n = positions.size();

        vector<tuple<int, int, char>> arr;
        for (int i = 0; i < n; i++) {
            arr.push_back({positions[i], healths[i], directions[i]});
        }
        sort(arr.begin(), arr.end());

        // stack
        vector<tuple<int, int, char>> st;

        for (auto& [pos, hp, dir] : arr) {
            if (dir == 'R') {
                st.push_back({pos, hp, dir});
            }
            else {
                bool can_push = true;
                while (!st.empty() && get<2>(st.back()) == 'R') {
                    int& collision_hp = get<1>(st.back());
                    if (collision_hp < hp) {
                        hp--;
                        st.pop_back();
                    }
                    else if (collision_hp == hp) {
                        st.pop_back();
                        can_push = false;
                        break;
                    }
                    else if (collision_hp > hp) {
                        can_push = false;
                        collision_hp -= 1;
                        break;
                    }
                }

                if (can_push) {
                    st.push_back({pos, hp, dir});
                }
            }
        }
        
        unordered_map<int, int> mp;
        for (auto& [pos, hp, dir] : st) {
            mp[pos] = hp;
        }

        vector<int> res;
        for (int pos : positions) {
            if (mp.count(pos)) {
                res.push_back(mp[pos]);
            }
        }

        return res;
    }
};
