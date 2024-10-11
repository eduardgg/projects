#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>

using namespace std;

struct Point {
    double x, y;
};

bool operator < (const Point& a, const Point& b) {
    return a.x < b.x || (a.x == b.x && a.y < b.y);
}

struct Line {
    // ax + by + c = 0
    double a, b, c; 
};

// Funció per trobar la línia perpendicular bisectora entre dos punts
Line perpendicularBisector(const Point& p1, const Point& p2) {
    double a = p2.y - p1.y;
    double b = p1.x - p2.x;
    double c = a * (p1.x + p2.x) / 2 + b * (p1.y + p2.y) / 2;
    return {a, b, -c};
}

// Funció per calcular l'intersecció entre dues línies
Point intersection(const Line& l1, const Line& l2) {
    double det = l1.a * l2.b - l2.a * l1.b;
    if (det == 0) throw runtime_error("Línies paral·leles");
    double x = (l2.b * l1.c - l1.b * l2.c) / det;
    double y = (l1.a * l2.c - l2.a * l1.c) / det;
    return {x, y};
}

// Funció per imprimir els punts del diagrama de Voronoi
void printVoronoi(const vector<Point>& points) {
    int n = points.size();
    vector<Line> bisectors;

    // Calcular bisectors per a cada parella de punts
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Line bisector = perpendicularBisector(points[i], points[j]);
            bisectors.push_back(bisector);
        }
    }

    // Trobar les interseccions dels bisectors
    for (int i = 0; i < bisectors.size(); ++i) {
        for (int j = i + 1; j < bisectors.size(); ++j) {
            try {
                Point p = intersection(bisectors[i], bisectors[j]);
                cout << "Punt de Voronoi a: (" << p.x << ", " << p.y << ")\n";
            } catch (const runtime_error& e) {
                // Les línies són paral·leles i no tenen intersecció
            }
        }
    }
}

int main() {

    vector<Point> points = {{0, 0}, {2, 0}, {1, 1}, {3, 3}, {2, 2}};
    printVoronoi(points);
    return 0;

}
