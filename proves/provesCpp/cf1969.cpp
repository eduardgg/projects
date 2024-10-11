#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {

    int t;
    cin >> t;

    while (t) {
        t--;
        int n, k;
        cin >> n >> k;
        vector<int> a(n, 0);
        vector<int> b(n, 0);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
        }

        vector<pair<int, int>> m;
        for (int i = 0; i < n; ++i) {
            m.push_back({b[i], a[i]});
        }
        sort(m.begin(), m.end(), greater<pair<int, int>>());

        vector<int> p(1, 0);
        for (int i = n - 1; i >= 0; --i) {
            p.push_back(p.back() + max(0, m[i].first - m[i].second));
        }
        reverse(p.begin(), p.end());

        priority_queue<int> h;
        int ben = 0;
        for (int i = 0; i < k; ++i) {
            h.push(m[i].second);
            ben -= m[i].second;
        }

        int top = max(0, ben + p[k]);

        for (int i = k; i < n; ++i) {
            h.push(m[i].second);
            ben -= m[i].second;
            ben += h.top();
            h.pop();
            top = max(top, ben + p[i + 1]);
        }

        cout << top << endl;
    }

    return 0;
}