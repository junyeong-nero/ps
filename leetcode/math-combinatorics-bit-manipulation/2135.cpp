class Solution {
public:

    int s2i(string s) {
        int res = 0;
        for (char c : s) {
            res |= (1 << (c - 'a'));
        }
        return res;
    }

    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        
        map<int,set<int>> d;

        for (string src : startWords) {
            d[src.size()].insert(s2i(src));
        }

        int res = 0;
        for (string target : targetWords) {

            int target_num = s2i(target);
            for (char c : target) {
                int temp = target_num ^ (1 << (c - 'a'));
                if (d[target.size() - 1].count(temp)) {
                    res++;
                    break;
                }
            }
        }

        return res; 
    }
};
