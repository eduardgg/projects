#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> P;
typedef vector<P> VP;

int main() {
    // Definir el vector de parells de nombres
    VP parells;

    // Llegir l'input
    int n;
    cout << "Quants parells de nombres vols ordenar? ";
    cin >> n;

    // Llegir els parells de nombres i emmagatzemar-los al vector
    for (int i = 0; i < n; ++i) {
        int a, b;
        cout << "Entra el primer nombre del parell " << i + 1 << ": ";
        cin >> a;
        cout << "Entra el segon nombre del parell " << i + 1 << ": ";
        cin >> b;
        parells.push_back(P(a, b));
    }

    // Ordenar el vector de parells de nombres
    sort(parells.begin(), parells.end());

    // Mostrar el vector ordenat
    cout << "El vector ordenat de parells de nombres és:\n";
    for (auto &p : parells) {
        cout << "(" << p.first << ", " << p.second << ")\n";
    }

    return 0;
}
