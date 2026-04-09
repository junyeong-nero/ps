class Solution {
public:
    int smallC[5][5] = {{1, 0, 0, 0, 0},
                        {1, 1, 0, 0, 0},
                        {1, 2, 1, 0, 0},
                        {1, 3, 3, 1, 0},
                        {1, 4, 1, 4, 1}};

    // C(n, k) mod 2
    int combMod2(int n, int k) { return ((k & (n - k)) == 0) ? 1 : 0; }

    // C(n, k) mod 5 using Lucas theorem
    int combMod5(int n, int k) {
        int res = 1;
        while (n > 0 || k > 0) {
            int ni = n % 5;
            int ki = k % 5;
            if (ki > ni)
                return 0;
            res = (res * smallC[ni][ki]) % 5;
            n /= 5;
            k /= 5;
        }
        return res;
    }

    // combine mod 2 and mod 5 -> mod 10
    int combMod10(int n, int k) {
        int a = combMod2(n, k);
        int b = combMod5(n, k);

        for (int x = 0; x < 10; x++) {
            if (x % 2 == a && x % 5 == b)
                return x;
        }
        return 0;
    }

    bool hasSameDigits(string s) {
        int n = s.size();
        int N = n - 2;

        int a = 0, b = 0;
        for (int k = 0; k <= N; k++) {
            int c = combMod10(N, k);
            a = (a + (s[k] - '0') * c) % 10;
            b = (b + (s[k + 1] - '0') * c) % 10;
        }

        return a == b;
    }
};
