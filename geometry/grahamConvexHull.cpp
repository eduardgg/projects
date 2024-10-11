#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>

using namespace std;

struct Point {
    int x, y;
};

// Funció de comparació per a ordenar els punts segons l'angle polar
bool compare(const Point& p1, const Point& p2) {
    return (p1.y < p2.y) || (p1.y == p2.y && p1.x < p2.x);
}

// Funció per calcular la direcció (colinearitat) entre tres punts
int orientation(const Point& p, const Point& q, const Point& r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;  // Colinear
    return (val > 0) ? 1 : 2; // 1 = Clockwise, 2 = Counterclockwise
}

// Algoritme de Graham's Scan per trobar el convex hull
vector<Point> grahamScan(vector<Point>& points) {
    int n = points.size();
    if (n < 3) return {}; // Un conjunt de punts ha de tenir almenys 3 punts per formar un convex hull

    // Trobar el punt inferior-esquerre
    Point p0 = *min_element(points.begin(), points.end(), compare);
    sort(points.begin(), points.end(), [&](const Point& p1, const Point& p2) {
        int o = orientation(p0, p1, p2);
        if (o == 0) return (pow(p1.x - p0.x, 2) + pow(p1.y - p0.y, 2)) < (pow(p2.x - p0.x, 2) + pow(p2.y - p0.y, 2));
        return o == 2;
    });

    vector<Point> hull;
    hull.push_back(p0);
    for (int i = 1; i < n; i++) {
        while (hull.size() > 1 && orientation(hull[hull.size() - 2], hull.back(), points[i]) != 2) {
            hull.pop_back();
        }
        hull.push_back(points[i]);
    }

    return hull;
}

// Funció per imprimir el convex hull
void printConvexHull(const vector<Point>& hull) {
    cout << "Convex Hull: \n";
    for (const auto& p : hull) {
        cout << "(" << p.x << ", " << p.y << ")\n";
    }
}

int main() {
    vector<Point> points = {{0, 0}, {2, 0}, {1, 1}, {3, 3}, {2, 2}, {4, 0}, {3, 1}};

    vector<Point> hull = grahamScan(points);

    printConvexHull(hull);

    return 0;
}
