#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class SegmentTree {
public:
    SegmentTree(const vector<int>& data) {
        n = data.size();
        treeMin.resize(4 * n, INT_MAX);
        treeMax.resize(4 * n, INT_MIN);
        build(data, 0, 0, n - 1);
    }

    // Consulta del mínim en un interval [l, r]
    int queryMin(int l, int r) {
        return queryMin(0, 0, n - 1, l, r);
    }

    // Consulta del màxim en un interval [l, r]
    int queryMax(int l, int r) {
        return queryMax(0, 0, n - 1, l, r);
    }

    // Actualització d'un valor a una posició específica
    void update(int idx, int value) {
        update(0, 0, n - 1, idx, value);
    }

private:
    vector<int> treeMin;
    vector<int> treeMax;
    int n;

    void build(const vector<int>& data, int node, int start, int end) {
        if (start == end) {
            treeMin[node] = data[start];
            treeMax[node] = data[start];
        } else {
            int mid = (start + end) / 2;
            build(data, 2 * node + 1, start, mid);
            build(data, 2 * node + 2, mid + 1, end);
            treeMin[node] = min(treeMin[2 * node + 1], treeMin[2 * node + 2]);
            treeMax[node] = max(treeMax[2 * node + 1], treeMax[2 * node + 2]);
        }
    }

    int queryMin(int node, int start, int end, int l, int r) {
        if (r < start || l > end) {
            // Valor neutral per al mínim
            return INT_MAX;
        }
        if (l <= start && end <= r) {
            return treeMin[node];
        }
        int mid = (start + end) / 2;
        int leftMin = queryMin(2 * node + 1, start, mid, l, r);
        int rightMin = queryMin(2 * node + 2, mid + 1, end, l, r);
        return min(leftMin, rightMin);
    }

    int queryMax(int node, int start, int end, int l, int r) {
        if (r < start || l > end) {
            // Valor neutral per al màxim
            return INT_MIN;
        }
        if (l <= start && end <= r) {
            return treeMax[node];
        }
        int mid = (start + end) / 2;
        int leftMax = queryMax(2 * node + 1, start, mid, l, r);
        int rightMax = queryMax(2 * node + 2, mid + 1, end, l, r);
        return max(leftMax, rightMax);
    }

    void update(int node, int start, int end, int idx, int value) {
        if (start == end) {
            treeMin[node] = value;
            treeMax[node] = value;
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid) {
                update(2 * node + 1, start, mid, idx, value);
            } else {
                update(2 * node + 2, mid + 1, end, idx, value);
            }
            treeMin[node] = min(treeMin[2 * node + 1], treeMin[2 * node + 2]);
            treeMax[node] = max(treeMax[2 * node + 1], treeMax[2 * node + 2]);
        }
    }
};

int main() {
    vector<int> data = {1, 3, 5, 7, 9, 11};
    SegmentTree segTree(data);

    cout << "Mínim en el interval [1, 4]: " << segTree.queryMin(1, 4) << endl;
    cout << "Màxim en el interval [1, 4]: " << segTree.queryMax(1, 4) << endl;

    cout << "Actualitzant l'índex 3 amb el valor 0" << endl;
    segTree.update(3, 0);

    cout << "Mínim en el interval [1, 4] després de l'actualització: " << segTree.queryMin(1, 4) << endl;
    cout << "Màxim en el interval [1, 4] després de l'actualització: " << segTree.queryMax(1, 4) << endl;

    return 0;
}
