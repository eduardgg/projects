#include <iostream>
#include <vector>

using namespace std;

int main() {
    int rows = 3; // Nombre de files
    int cols = 4; // Nombre de columnes

    // Crear una matriu de 3 files i 4 columnes, inicialitzada amb zeros
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));

    // Assignar valors a la matriu
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            matrix[i][j] = i * cols + j + 1;
        }
    }

    // Imprimir la matriu
    cout << "Matriu:" << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}