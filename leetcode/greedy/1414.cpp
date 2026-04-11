class Solution {
public:

    vector<int> get_fib(int k) {
        vector<int> fib = {1, 1};
        while (fib.back() < k) {
            int n = fib.size();
            fib.push_back(fib[n - 1] + fib[n - 2]);
        }
        return fib;
    }

    int findMinFibonacciNumbers(int k) {

        vector<int> fib = get_fib(k);
        int res = 0;

        while (k > 0) {
            auto it = lower_bound(fib.begin(), fib.end(), k);
            if (*it > k)
                it -= 1;

            cout << *it << endl;
            k -= *it;
            res++;
        }
    
        return res;
    }
};
