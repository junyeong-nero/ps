#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <deque>
#include <queue>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <random>

using namespace std;

void defaultdict_example() {
    unordered_map<int, vector<int>> graph;
    vector<pair<int, int>> edges = {{1, 2}, {2, 3}, {1, 3}};

    for (auto [u, v] : edges) {
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (auto& [node, neighbors] : graph) {
        cout << node << ": ";
        for (int nxt : neighbors) cout << nxt << ' ';
        cout << '\n';
    }
}


void counter_example() {
    vector<int> arr1, arr2;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(1, 10);

    for (int i = 1; i < 10; i++) {
        int c1 = dist(gen);
        int c2 = dist(gen);

        for (int j = 0; j < c1; j++) arr1.push_back(i);
        for (int j = 0; j < c2; j++) arr2.push_back(i);
    }

    unordered_map<int, int> counter1, counter2;
    for (int x : arr1) counter1[x]++;
    for (int x : arr2) counter2[x]++;

    cout << "counter1:\n";
    for (auto [k, v] : counter1) cout << k << ": " << v << '\n';

    cout << "counter2:\n";
    for (auto [k, v] : counter2) cout << k << ": " << v << '\n';

    cout << "counter1 + counter2:\n";
    unordered_map<int, int> plus_counter = counter1;
    for (auto [k, v] : counter2) plus_counter[k] += v;
    for (auto [k, v] : plus_counter) cout << k << ": " << v << '\n';

    cout << "counter1 - counter2 (positive only):\n";
    unordered_map<int, int> minus_counter;
    for (auto [k, v] : counter1) {
        int diff = v - counter2[k];
        if (diff > 0) minus_counter[k] = diff;
    }
    for (auto [k, v] : minus_counter) cout << k << ": " << v << '\n';
}


void deque_example() {
    deque<pair<int, int>> q;

    q.push_back({1, 2});
    q.push_front({3, 4});
    q.push_back({5, 6});

    q.pop_front();
    q.pop_back();

    q.clear();
}


void heapq_example() {
    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;

    pq.push({2, "b"});
    pq.push({1, "a"});
    pq.push({3, "c"});

    while (!pq.empty()) {
        auto [x, y] = pq.top();
        pq.pop();
        cout << x << ' ' << y << '\n';
    }
}


void itertools_example() {
    vector<int> arr = {1, 2, 3};

    cout << "permutations:\n";
    sort(arr.begin(), arr.end());
    do {
        for (int x : arr) cout << x << ' ';
        cout << '\n';
    } while (next_permutation(arr.begin(), arr.end()));

    cout << "accumulate:\n";
    vector<int> prefix(arr.size());
    partial_sum(arr.begin(), arr.end(), prefix.begin());
    for (int x : prefix) cout << x << ' ';
    cout << '\n';

    cout << "product (manual):\n";
    vector<int> nums = {1, 2};
    for (int a : nums) {
        for (int b : nums) {
            cout << "(" << a << ", " << b << ") ";
        }
    }
    cout << '\n';
}


int fib_memo(int n, vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
}

void functools_example() {
    vector<int> memo(100, -1);
    cout << fib_memo(10, memo) << '\n';
}


void math_example() {
    cout << gcd(12, 18) << '\n';
    cout << "comb(5, 2): ";

    long long comb = 1;
    int n = 5, r = 2;
    for (int i = 0; i < r; i++) {
        comb = comb * (n - i) / (i + 1);
    }
    cout << comb << '\n';

    cout << sqrt(81) << '\n';
    cout << ceil(3.14) << '\n';
    cout << floor(3.14) << '\n';
}


void set_example() {
    unordered_set<int> s;

    s.insert(1);
    s.insert(2);
    s.insert(2);

    cout << "set contents: ";
    for (int x : s) cout << x << ' ';
    cout << '\n';

    set<int> a = {1, 2, 3};
    set<int> b = {3, 4, 5};

    cout << "union: ";
    set<int> union_set;
    set_union(a.begin(), a.end(), b.begin(), b.end(),
              inserter(union_set, union_set.begin()));
    for (int x : union_set) cout << x << ' ';
    cout << '\n';

    cout << "intersection: ";
    set<int> inter_set;
    set_intersection(a.begin(), a.end(), b.begin(), b.end(),
                     inserter(inter_set, inter_set.begin()));
    for (int x : inter_set) cout << x << ' ';
    cout << '\n';

    cout << "difference: ";
    set<int> diff_set;
    set_difference(a.begin(), a.end(), b.begin(), b.end(),
                   inserter(diff_set, diff_set.begin()));
    for (int x : diff_set) cout << x << ' ';
    cout << '\n';

    cout << (a.count(2) ? "2 in a" : "2 not in a") << '\n';
}


void list_example() {
    vector<int> arr = {3, 1, 4, 1, 5};

    arr.push_back(9);
    arr.insert(arr.end(), {2, 6});
    sort(arr.begin(), arr.end());

    for (int x : arr) cout << x << ' ';
    cout << '\n';

    cout << arr[0] << '\n';
    cout << arr.back() << '\n';

    cout << "first 3: ";
    for (int i = 0; i < 3; i++) cout << arr[i] << ' ';
    cout << '\n';

    reverse(arr.begin(), arr.end());
    for (int x : arr) cout << x << ' ';
    cout << '\n';

    cout << "count of 1: " << count(arr.begin(), arr.end(), 1) << '\n';

    auto it = find(arr.begin(), arr.end(), 5);
    if (it != arr.end()) {
        cout << "index of 5: " << (it - arr.begin()) << '\n';
    }
}


int main() {
    return 0;
}