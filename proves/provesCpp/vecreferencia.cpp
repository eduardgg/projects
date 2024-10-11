#include <iostream>
#include <vector>

using namespace std;


void func() {
    // Al·loquem memòria al heap:
    int* ptr = new int(10);
    // Aquí podem usar "ptr" i la memòria al heap:
    cout << "Valor: " << *ptr << endl;
    // Allibera la memòria al heap
    delete ptr;
}

void modificaVector(vector<int> &v) {
    for (int i = 0; i < v.size(); i++) {
        // Modifiquem la còpia del vector dins la funció:
        v[i] += 10;
    }
}

int main() {
    vector<int> v = {1, 2, 3, 4, 5};

    cout << "Vector original abans de modificar: ";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // Passem el vector per valor (còpia):
    modificaVector(v);

    cout << "Vector original després de modificar: ";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // int *arr = (int*) malloc(10 * sizeof(int)); // C
    // int *arr = new int[10]; // C++
    int arr[10];
    arr[3] = 7;
    cout << arr[3] << endl;
    cout << arr[5] << endl;

    func();




    return 0;
}
