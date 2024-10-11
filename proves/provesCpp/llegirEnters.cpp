#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> stringToIntVec(const string& str) {
    vector<int> result;
    istringstream iss(str);
    int num;
    while (iss >> num) {
        result.push_back(num);
    }
    return result;
}


int main() {
    cout << endl;
    ifstream fitxer("exemple.txt");
    if (!fitxer) {
        cerr << "No s'ha pogut obrir el fitxer" << endl;
        return 1;
    }

    string linia;
    while (getline(fitxer, linia)) {
        cout << linia << endl;
        vector<int> v = stringToIntVec(linia);
        for (int i = 0; i < v.size(); ++ i) {
            cout << v[i] << (i < v.size() - 1 ? ", " : "");
        }
        cout << endl;
    }

    fitxer.close();
    return 0;
}
