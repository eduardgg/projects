#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Point {
    double x, y;
};

// Funció per comparar dos punts segons la coordenada x, i després la y
bool compare(const Point& p1, const Point& p2) {
    return p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y);
}

// Calcula l'àrea del triangle format per tres punts
double area(const Point& p1, const Point& p2, const Point& p3) {
    return fabs((p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)) / 2.0);
}

// Comprova si un punt està dins del cercle circumcirculant del triangle
bool isInCircumcircle(const Point& p, const Point& p1, const Point& p2, const Point& p3) {
    double ax = p1.x - p.x;
    double ay = p1.y - p.y;
    double bx = p2.x - p.x;
    double by = p2.y - p.y;
    double cx = p3.x - p.x;
    double cy = p3.y - p.y;

    double det = ax * (by * cy - cy * by) - ay * (bx * cy - cx * by) + (ax * (bx * by - cx * by) - ay * (bx * cx - cx * bx));
    return det > 0;
}

// Algorisme Incremental per a la Triangulació de Delaunay
vector<vector<Point>> delaunayTriangulation(vector<Point>& points) {
    vector<vector<Point>> triangles;

    // Ordena els punts per x i després per y
    sort(points.begin(), points.end(), compare);

    // Inicialització amb el triangle gran que conté tots els punts
    Point p1 = {0, 0}; // Ajusta aquests punts a una gran àrea que conté tots els punts
    Point p2 = {1000, 0};
    Point p3 = {0, 1000};
    triangles.push_back({p1, p2, p3});

    for (const Point& p : points) {
        vector<vector<Point>> newTriangles;

        for (const vector<Point>& triangle : triangles) {
            if (isInCircumcircle(p, triangle[0], triangle[1], triangle[2])) {
                newTriangles.push_back({triangle[0], triangle[1], p});
                newTriangles.push_back({triangle[1], triangle[2], p});
                newTriangles.push_back({triangle[2], triangle[0], p});
            } else {
                newTriangles.push_back(triangle);
            }
        }

        triangles = newTriangles;
    }

    return triangles;
}

// Funció per imprimir els triangles
void printTriangles(const vector<vector<Point>>& triangles) {
    cout << "Triangulació de Delaunay:\n";
    for (const auto& triangle : triangles) {
        cout << "Triangle: \n";
        for (const auto& p : triangle) {
            cout << "(" << p.x << ", " << p.y << ")\n";
        }
        cout << "\n";
    }
}

int main() {
    vector<Point> points = {{0, 0}, {2, 0}, {1, 1}, {3, 3}, {2, 2}};

    vector<vector<Point>> triangles = delaunayTriangulation(points);

    printTriangles(triangles);

    return 0;
}
