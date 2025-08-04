#include <iostream>
#include <vector>

using namespace std;

void f(int i, int a, int n, vector<int> v) {
    if (i == n) {
        for (int e : v) {
            cout << e << " ";
        }
        cout << endl;
        return;
    }
    for (int k=1; k <= a; ++k) {
        v[i] = k;
        f(i+1, a, n, v);
    }
}


int main()
{   
    int n = 3;
    int a = 4;
    vector<int> v(n, 0);
    f(0, a, n, v);
}