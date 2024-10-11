#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {

    // Sembla que el heap ignora valors <= 0
    // La funció top retorna el més gran!
    priority_queue<int> h;

    h.push(5);
    h.push(8);
    int a = h.top();
    h.pop();
    h.push(-3);
    h.push(0);
    h.push(10);
    int b = h.top();
    int c = h.top();
    int size = h.size();
    cout << endl << a << " " << b << " " << c << " " << size << endl;
    while (h.top()) {
        cout << h.top() << " ";
        h.pop();
    }

    return 0;
}