#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int t = 0; t < n; t++) {
        int x;
        cin >> x;
        double total = 0.0;
        for (int i = 0; i < x; i++) {
            string name;
            int quantity;
            double price;
            cin >> name >> quantity >> price;
            total += quantity * price;
        }
        cout << "$" << fixed << setprecision(2) << total << endl;
    }
    return 0;
}
