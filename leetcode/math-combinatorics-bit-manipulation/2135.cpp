class Solution {
public:
    int s2i(string& s) {
        int ret = 0;
        for (int i = 0; i < s.length(); i++)
            ret |= (1 << (s[i] - 'a'));
        return ret;
    }

    int wordCount(vector<string>& sw, vector<string>& tw) {
        set<int> st;
        int ans = 0;
        for (auto& s : sw)
            st.insert(s2i(s));
        for (auto& s : tw) {
            int n = s2i(s);
            for (int i = 0; i < 26; i++)
                if (n & (1 << i)) {
                    if (st.find(n ^ (1 << i)) != st.end()) {
                        ans++;
                        break;
                    }
                }
        }
        return ans;
    }
};
